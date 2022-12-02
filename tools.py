import weather
import pandas as pd 
import plotly.graph_objects as go

def loc_att(city, dis):
    temp , hum = weather.weather(city)
    rf=pd.read_csv(r'./resources/raw/rainfall.csv')
    rnf = rf[rf['district']==dis.upper()]['rainfall']
    return [temp,hum,rnf]  

def graph_val(out):
    df=pd.read_csv('./resources/raw/FertilizerData.csv')
    N = df[df['Crop']==out]['N'].iloc[0]
    P = df[df['Crop']==out]['P'].iloc[0]
    K = df[df['Crop']==out]['K'].iloc[0]
    ph =df[df['Crop']==out]['pH'].iloc[0]
    ca = df[df['Crop']==out]['calcium'].iloc[0]
    mg= df[df['Crop']==out]['magnesium'].iloc[0]
    s = df[df['Crop']==out]['sulphur'].iloc[0]
    b =df[df['Crop']==out]['boron'].iloc[0]
    zn = df[df['Crop']==out]['zinc'].iloc[0]
    fe = df[df['Crop']==out]['iron'].iloc[0]
    mn = df[df['Crop']==out]['magnese'].iloc[0]
    opt =[N,P,K,ca,mg,s,b,fe,zn,mn,ph]
    
    return(opt)


    
def graph(req):
    fig = go.Figure()
    x=['Nitrogen','potassium','Phosporous','calcium','magnesium','sulphur','boron','iron','zinc','manganese','ph']
    fig.add_bar(y=x,x=req,orientation='h',width=0.5,name='available',marker = dict(color=' rgb(10, 24, 219)' ))

    #fig.show()
    fig.layout.template = "plotly_dark"
    return fig
    