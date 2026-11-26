# %% imports and rendering setup
from pathlib import Path
import os, sys, json, base64, hashlib, ctypes, platform, copy
import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.io as pio
from IPython.display import Image, display

folder = Path.cwd()
figures = folder / 'figures'
figures.mkdir(exist_ok=True)
fonts = folder / 'assets' / 'fonts'
data = pd.read_csv(folder / 'annual_analysis.csv')
sensitivity = pd.read_csv(folder / 'all_base_year_sensitivity.csv')
purple, teal, ink, muted, grid = '#6842B8', '#147D82', '#172127', '#53616A', '#EEF0F2'
body_font, title_font = 'IBM Plex Sans', 'IBM Plex Sans Condensed'
if not os.environ.get('BROWSER_PATH'):
    cached = Path.home() / 'Library/Caches/ms-playwright/chromium_headless_shell-1234/chrome-headless-shell-mac-arm64/chrome-headless-shell'
    if cached.is_file(): os.environ['BROWSER_PATH'] = str(cached)

# %% font registration and embedding
font_specs = [
 ('IBMPlexSans-Regular.ttf',body_font,400,'normal'),
 ('IBMPlexSans-Medium.ttf',body_font,500,'normal'),
 ('IBMPlexSans-SemiBold.ttf',body_font,600,'normal'),
 ('IBMPlexSans-Italic.ttf',body_font,400,'italic'),
 ('IBMPlexSansCondensed-Regular.ttf',title_font,400,'normal'),
 ('IBMPlexSansCondensed-Medium.ttf',title_font,500,'normal'),
 ('IBMPlexSansCondensed-SemiBold.ttf',title_font,600,'normal')]
font_css = ''
for file, family, weight, style in font_specs:
    encoded = base64.b64encode((fonts / file).read_bytes()).decode()
    font_css += f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};src:url(data:font/ttf;base64,{encoded}) format('truetype');}}\n"

if platform.system() == 'Darwin':
    cf = ctypes.CDLL('/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation')
    ct = ctypes.CDLL('/System/Library/Frameworks/CoreText.framework/CoreText')
    cf.CFURLCreateFromFileSystemRepresentation.argtypes = [ctypes.c_void_p,ctypes.c_char_p,ctypes.c_long,ctypes.c_bool]
    cf.CFURLCreateFromFileSystemRepresentation.restype = ctypes.c_void_p
    cf.CFRelease.argtypes = [ctypes.c_void_p]
    cf.CFArrayGetCount.argtypes = [ctypes.c_void_p]; cf.CFArrayGetCount.restype = ctypes.c_long
    cf.CFArrayGetValueAtIndex.argtypes = [ctypes.c_void_p,ctypes.c_long]; cf.CFArrayGetValueAtIndex.restype = ctypes.c_void_p
    cf.CFStringGetCString.argtypes = [ctypes.c_void_p,ctypes.c_char_p,ctypes.c_long,ctypes.c_uint32]; cf.CFStringGetCString.restype = ctypes.c_bool
    ct.CTFontManagerCopyAvailablePostScriptNames.restype = ctypes.c_void_p
    ct.CTFontManagerRegisterFontsForURL.argtypes = [ctypes.c_void_p,ctypes.c_uint32,ctypes.POINTER(ctypes.c_void_p)]
    ct.CTFontManagerRegisterFontsForURL.restype = ctypes.c_bool
    ct.CTFontManagerUnregisterFontsForURL.argtypes = ct.CTFontManagerRegisterFontsForURL.argtypes
    ct.CTFontManagerUnregisterFontsForURL.restype = ctypes.c_bool

def plex_names():
    if platform.system() != 'Darwin': return []
    names = ct.CTFontManagerCopyAvailablePostScriptNames()
    found = []
    for index in range(cf.CFArrayGetCount(names)):
        value = cf.CFArrayGetValueAtIndex(names,index); buffer = ctypes.create_string_buffer(256)
        if cf.CFStringGetCString(value,buffer,256,0x08000100) and buffer.value.startswith(b'IBMPlex'):
            found.append(buffer.value.decode())
    cf.CFRelease(names)
    return sorted(found)

# %% common layout and truthful axes

def chart_layout(fig, title, subtitle, x_range, y_range, y_ticks, x_ticks):
    fig.update_layout(template='none',width=1200,height=760,paper_bgcolor='white',plot_bgcolor='white',
        font=dict(family=body_font,size=18,color=ink),margin=dict(l=82,r=58,t=120,b=150),
        title=dict(text=title,x=0.068,y=0.96,xanchor='left',yanchor='top',
            font=dict(family=title_font,size=36,weight=600,color=ink),
            subtitle=dict(text=subtitle,font=dict(family=body_font,size=19,color=muted))),hovermode='x unified')
    fig.update_xaxes(range=x_range,tickvals=x_ticks,tickfont=dict(size=18),showgrid=False,zeroline=False,
        showline=True,linecolor='#B8C0C5',linewidth=1,ticks='')
    fig.update_yaxes(range=y_range,tickvals=y_ticks,tickfont=dict(size=18),showgrid=True,gridcolor=grid,
        gridwidth=1,zeroline=False,showline=False,ticks='')
    return fig

def source_footer(fig, first, second):
    for y, text in [(-0.19,first),(-0.245,second)]:
        fig.add_annotation(x=0,y=y,xref='paper',yref='paper',text=text,showarrow=False,xanchor='left',
            align='left',font=dict(family=body_font,size=14,color=muted),name='source-footer')

# %% export static vectors, report layout, and fully local interactive HTML
export_log = []
def export_chart(fig, stem, table, alt_text):
    report = go.Figure(fig)
    report.update_layout(height=620,margin=dict(l=90,r=100,t=110,b=140))
    report.update_xaxes(tickfont=dict(size=24))
    report.update_yaxes(tickfont=dict(size=24))
    report.layout.title.font.size = 34
    report.layout.title.subtitle.font.size = 22
    report.layout.legend.font.size = 21
    for annotation in report.layout.annotations:
        if annotation.name != 'source-footer':
            annotation.font.size = 20 if annotation.text in ['Near-flat, 2019–2021', '2013 relationship', '100 = unchanged'] else 24
    footer = [a for a in report.layout.annotations if a.name == 'source-footer']
    for annotation, y in zip(footer,[-0.22,-0.31]):
        annotation.y = y
        annotation.font.size = 20
        annotation.text = annotation.text.replace('Source: DSEC RPPI releases, Employment Survey 2013 and Economic Bulletin Table V.5.', 'Sources: DSEC RPPI releases; Employment Survey 2013; Economic Bulletin V.5.')
    before = plex_names(); owned = []
    try:
        if platform.system() == 'Darwin':
            for file, family, weight, style in font_specs:
                path = str(fonts/file).encode()
                url = cf.CFURLCreateFromFileSystemRepresentation(None,path,len(path),False)
                error = ctypes.c_void_p()
                if ct.CTFontManagerRegisterFontsForURL(url,3,ctypes.byref(error)): owned.append(url)
                else: cf.CFRelease(url)
        paths = [figures/f'{prefix}{stem}.{extension}' for prefix in ['', 'report_'] for extension in ['png','pdf','svg']]
        pio.write_images(fig=[fig]*3+[report]*3,file=paths,format=['png','pdf','svg']*2,
            width=[1200]*6,height=[760]*3+[620]*3,scale=[2,1,1]*2)
    finally:
        if platform.system() == 'Darwin':
            for url in owned:
                error = ctypes.c_void_p()
                assert ct.CTFontManagerUnregisterFontsForURL(url,3,ctypes.byref(error))
                cf.CFRelease(url)
            assert plex_names() == before
    for path in [figures/f'{stem}.svg', figures/f'report_{stem}.svg']:
        svg = path.read_text(); position = svg.find('>',svg.find('<svg'))+1
        svg = svg[:position]+'<defs><style><![CDATA['+font_css+']]></style></defs>'+svg[position:]
        path.write_text(svg)
    fig.write_json(figures/f'{stem}.plotly.json')
    html = fig.to_html(include_plotlyjs=True,include_mathjax=False,full_html=True,
        config=dict(displaylogo=False,responsive=True,scrollZoom=False,toImageButtonOptions=dict(format='svg',filename=stem)))
    style = font_css + "body{margin:0;color:#172127;background:white;font-family:'IBM Plex Sans',sans-serif}main{max-width:1200px;margin:auto;padding:0 28px 36px}.chart-scroll{overflow-x:auto}.plotly-graph-div{min-width:960px}table{border-collapse:collapse;width:100%;font-size:16px;font-variant-numeric:tabular-nums}th,td{text-align:right;padding:9px 12px;border-bottom:1px solid #EEF0F2}th:first-child,td:first-child{text-align:left}summary{cursor:pointer;padding:20px 0;font-weight:500}a:focus-visible,summary:focus-visible{outline:2px solid #6842B8;outline-offset:4px}::selection{background:#e4daf8;color:#172127}p{line-height:1.6}"
    html = html.replace('</head>','<style>'+style+'</style></head>')
    html = html.replace('<body>','<body><main><div class="chart-scroll" role="img" aria-label="'+alt_text+'">')
    html = html.replace('</body>','</div><p>'+alt_text+'</p><details><summary>Annual values</summary>'+table.to_html(index=False,border=0,float_format=lambda x:f'{x:.2f}')+'</details></main></body>')
    (figures/f'{stem}.html').write_text(html)
    export_log.append({'stem':stem,'standard_dimensions':[1200,760],'report_dimensions':[1200,620],
        'temporary_session_fonts_registered':len(owned),'session_fonts_restored':plex_names()==before,
        'svg_embedded_font_faces':7,'html_plotly_inlined':True,'html_mathjax_disabled':True})
    (folder/'visual_export_log.json').write_text(json.dumps(export_log,indent=2))
    display(Image(filename=str(figures/f'{stem}.png')))

# %% common-base chart
trend = go.Figure()
trend.add_trace(go.Scatter(x=data.year,y=data.price_index_2013_100,mode='lines+markers',name='Housing prices',
    line=dict(color=purple,width=3.5),marker=dict(color=purple,size=8,symbol='circle',line=dict(color='white',width=1)),
    hovertemplate='%{x}<br>Housing prices: %{y:.1f}<extra></extra>'))
trend.add_trace(go.Scatter(x=data.year,y=data.earnings_index_2013_100,mode='lines+markers',name='Resident earnings',
    line=dict(color=teal,width=3,dash='dash'),marker=dict(color=teal,size=8,symbol='square',line=dict(color='white',width=1)),
    hovertemplate='%{x}<br>Resident earnings: %{y:.1f}<extra></extra>'))
chart_layout(trend,'Housing prices and resident earnings','Annual indices, 2013 = 100',
    [2012.7,2027.0],[80,155],[80,100,120,140],[2013,2015,2017,2019,2021,2023,2025])
trend.update_layout(showlegend=False)
trend.add_hline(y=100,line_color='#A1ABB2',line_width=1.2)
for y, text, color in [(data.earnings_index_2013_100.iloc[-1],'<b>Resident earnings</b><br>136.7',teal),
                        (data.price_index_2013_100.iloc[-1],'<b>Housing prices</b><br>104.0',purple)]:
    trend.add_annotation(x=2025.35,y=float(y),text=text,showarrow=False,xanchor='left',align='left',bgcolor='white',borderpad=2,font=dict(family=body_font,size=20,color=color))
trend.add_annotation(x=2020,y=142.0212765957,text='Near-flat, 2019–2021',showarrow=True,arrowhead=0,
    arrowcolor=muted,arrowwidth=1,ax=-20,ay=-42,font=dict(family=body_font,size=17,color=muted),bgcolor='white',borderpad=4)
source_footer(trend,'Source: DSEC RPPI releases, Employment Survey 2013 and Economic Bulletin Table V.5.',
    'Nominal annual values. Index axis starts at 80.')
export_chart(trend,'01_common_base_trends',data[['year','rppi_2011_100','resident_earnings_mop','price_index_2013_100','earnings_index_2013_100']],
    'The price index ends at 104.0 and the resident earnings index at 136.7 in 2025, with 2013 equal to 100. Annual observations are joined by straight lines.')

# %% annual-growth chart, retaining zero and the earnings hatch
annual = data.loc[data.year.gt(2013)]
growth = go.Figure()
growth.add_trace(go.Bar(x=annual.year-0.18,y=annual.rppi_growth_pct,width=0.34,name='Housing prices',
    marker=dict(color=purple),customdata=annual.year,hovertemplate='%{customdata}<br>Housing prices: %{y:.2f}%<extra></extra>'))
growth.add_trace(go.Bar(x=annual.year+0.18,y=annual.earnings_growth_pct,width=0.34,name='Resident earnings',
    marker=dict(color=teal,pattern=dict(shape='/',bgcolor=teal,fillmode='overlay',fgcolor='white',fgopacity=0.7,size=7,solidity=0.18)),
    customdata=annual.year,hovertemplate='%{customdata}<br>Resident earnings: %{y:.2f}%<extra></extra>'))
zeros = annual.loc[annual.earnings_growth_pct.eq(0)]
growth.add_trace(go.Scatter(x=zeros.year+0.18,y=zeros.earnings_growth_pct,mode='markers',showlegend=False,
    marker=dict(color=teal,size=4,symbol='square'),hoverinfo='skip'))
chart_layout(growth,'Annual change in prices and earnings','Change from the previous year (%)',
    [2013.4,2025.6],[-18,35],[-10,0,10,20,30],list(range(2014,2026)))
growth.update_layout(barmode='overlay',legend=dict(orientation='h',x=1,y=1.06,xanchor='right',yanchor='bottom',font=dict(size=17)))
growth.add_hline(y=0,line_color='#687780',line_width=1.4)
for x,y,text,color,shift in [(2013.82,28.2446808511,'+28.2%',purple,17),(2015.18,20,'+20.0%',teal,17),(2023.82,-11.7021276596,'−11.7%',purple,-18)]:
    growth.add_annotation(x=x,y=y,text=text,showarrow=False,yshift=shift,xanchor='left' if x==2013.82 else 'center',font=dict(family=body_font,size=18,color=color))
source_footer(growth,'Source: DSEC published annual RPPI and employed-resident earnings levels.',
    '2013 growth is unavailable. Small teal marks show zero change.')
export_chart(growth,'02_annual_growth',annual[['year','rppi_growth_pct','earnings_growth_pct']],
    'Annual growth compares consecutive years. Prices rise most in 2014 and fall most in 2024. Teal hatched bars show resident earnings; small teal marks show zero change.')

# %% relative-pressure chart
pressure = go.Figure(go.Scatter(x=data.year,y=data.relative_pressure_2013_100,mode='lines+markers',name='Relative pressure',
    line=dict(color=purple,width=3.5),marker=dict(color=purple,size=8,symbol='diamond',line=dict(color='white',width=1)),
    hovertemplate='%{x}<br>Relative pressure: %{y:.1f}<extra></extra>'))
chart_layout(pressure,'Relative change in prices compared with earnings','Relative pressure index, 2013 = 100',
    [2012.7,2027.0],[60,140],[60,80,100,120],[2013,2015,2017,2019,2021,2023,2025])
pressure.update_layout(showlegend=False)
pressure.add_hline(y=100,line_color='#A1ABB2',line_width=1.2,line_dash='dash')
pressure.add_annotation(x=2025.35,y=76.0897768552,text='<b>2025</b><br>76.1',showarrow=False,xanchor='left',
    align='left',font=dict(family=body_font,size=22,color=purple))
pressure.add_annotation(x=2014,y=128.2446808511,text='2014: 128.2',showarrow=False,yshift=24,font=dict(family=body_font,size=18,color=ink))
pressure.add_annotation(x=2025.35,y=100,text='2013 relationship',showarrow=False,xanchor='left',bgcolor='white',borderpad=2,font=dict(family=body_font,size=16,color=muted))
source_footer(pressure,'Calculated from DSEC annual RPPI and employed-resident earnings.',
    '100 × rebased RPPI / rebased earnings. Index axis starts at 60.')
export_chart(pressure,'03_relative_price_pressure',data[['year','relative_pressure_2013_100']],
    'Relative price pressure is 76.1 in 2025 with 2013 equal to 100. This compares changes since the base year and is not a household affordability ratio.')

# %% all-base-year sensitivity, with a true zero baseline
bases = go.Figure(go.Bar(x=sensitivity.base_year,y=sensitivity.relative_pressure_2025,name='Relative pressure in 2025',
    marker=dict(color=purple),width=0.60,text=sensitivity.relative_pressure_2025,texttemplate='%{text:.1f}',textposition='outside',
    textfont=dict(family=body_font,size=18,color=ink),hovertemplate='Base year %{x}<br>2025 pressure: %{y:.2f}<extra></extra>'))
chart_layout(bases,'The starting year changes the size of the comparison','Relative pressure in 2025, each base year = 100',
    [2012.4,2024.8],[0,112],[0,20,40,60,80,100],list(range(2013,2025)))
bases.update_layout(showlegend=False)
bases.add_hline(y=100,line_color='#7E8B93',line_width=1.2,line_dash='dash')
bases.add_annotation(x=2024.65,y=102,text='100 = unchanged',showarrow=False,xanchor='right',yshift=8,bgcolor='white',borderpad=2,font=dict(family=body_font,size=16,color=muted))
source_footer(bases,'Calculated from DSEC annual RPPI and employed-resident earnings.',
    'All 12 earlier observed bases are shown. Comparison periods differ.')
export_chart(bases,'04_all_base_year_sensitivity',sensitivity,
    'All 12 earlier observed base years give a 2025 pressure index below 100. The range is 59.3 for base 2014 to 90.6 for base 2024; the comparison periods differ.')

# %% rendering versions
import importlib.metadata
visual_versions = {'python':platform.python_version(),'plotly':plotly.__version__,
    'kaleido':importlib.metadata.version('kaleido'),'fonts':'IBM Plex Sans and Sans Condensed, bundled OFL files',
    'palette':{'prices':purple,'earnings':teal,'ink':ink,'grid':grid},'smoothing':False,'dual_axes':False}
(folder/'visual_export_versions.json').write_text(json.dumps(visual_versions,indent=2))
print('Saved four redesigned charts, report variants, Plotly specifications and offline interactive HTML.')
