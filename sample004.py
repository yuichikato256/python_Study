def plot_chart( df ,target_symbol ,start ,end ) :
  import plotly.graph_objs as go
  layout = dict( title = f'{target_symbol}: {start} ～ {end}'
                ,width = 1200 ,height = 600 ,font = dict( size=15 )
                ,xaxis = dict( title="" ,rangeslider=dict( visible=False ) ,showgrid=True ,tickangle=45 ) #type="Date"
                ,yaxis = dict( title="" ) )
  def add_scatter( fig ,df ,column_name ,**kwargs ) : fig.add_trace( go.Scatter( x=df.index ,y=df[ column_name ] ,name=column_name ,**kwargs ) )
  def add_candle( fig ,df ,**kwargs ) : fig.add_trace( go.Candlestick( x=df.index ,open=df['Open'] ,high=df['High'] ,low=df['Low'], close=df['Close'] ,showlegend=False ,**kwargs ) )

  df_plot = df.loc[ start : end ,: ]
  fig = go.Figure( data=[] )
  add_scatter( fig ,df_plot ,'Highest20' ,line=dict( color='rgba(150,150,150,.7)' ,width=1 ) )
  add_scatter( fig ,df_plot ,'Lowest20'  ,line=dict( color='rgba(150,150,150,.7)' ,width=1 ) ,fill="tonexty" ,fillcolor="rgba(120,120,120,.2)" )
  add_scatter( fig ,df_plot ,'Highest10' ,line=dict( color='rgba(100,100,100,.7)' ,width=1 ) )
  add_scatter( fig ,df_plot ,'Lowest10'  ,line=dict( color='rgba(100,100,100,.7)' ,width=1 ) ,fill="tonexty" ,fillcolor="rgba(70,70,70,.1)" )
  add_scatter( fig ,df_plot ,'EMA25'     ,line=dict( color='rgba(255,33,33,1)' ,width=1 ) )
  add_scatter( fig ,df_plot ,'EMA350'    ,line=dict( color='rgba(17,71,197,1)' ,width=1 ) )
  for col in df_plot.columns : 
    if 'L' in col and len( col )==2 : add_scatter( fig ,df_plot ,col ,line=dict( color='rgba(255,33,33,.7)' ,width=1 ) )
    if 'S' in col and len( col )==2 : add_scatter( fig ,df_plot ,col ,line=dict( color='rgba(17,71,197,.7)' ,width=1 ) )
  add_scatter( fig ,df_plot ,'ExitPrice' ,line=dict( color='rgba(38,38,38,1)'  ,width=2.5 ) )
  add_candle( fig ,df_plot )

  fig.update_layout( **layout )
  enable_plotly_in_cell()
  fig.show()

target_symbol = 'Eurodollar'
start = '2007-1-1'
end = '2019-12-31'

if __name__=='__main__' :
  plot_chart( backtest.chart[ target_symbol ].set_index( 'Time' ) ,target_symbol ,start ,end )