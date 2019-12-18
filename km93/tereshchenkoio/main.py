import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BiqQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('biqquerry-public-data','epa-historical-air-quality')


QUERY = """
        SELECT state_name, date_gmt, sample_measurement, units_of_measurement 
        FROM `biqquarry-public_data.epa-historical-air-quality.co_hourly_summary`
        LIMIT 10
        """


df = bq_assistant.query_to_pandas(QUERY)
df_measurement_state = df.groupby(['state_name'])['sample_measurement'].average
df_units_of_measure = df.groupby(['date_gmt'])['units_of_measure'].count()




trace1 = go.Scatter(
    x=df.measurement_state.index,
    y=df.measurement_state.values,
    mode = "lines",

                    )



trace2 = go.Pie(
    labels = df.units_of_measure.index,
    values = df.units_of_measure.values,


                    )

trace3 = go.Bar(
    x=df.measurement_state.index,
    y=df.measurement_state.values,
    name = "measurement in state",

)

data = [trace1]

layout = dict(
              title = 'measurement',
              xaxis= dict(title= 'state'),
              yaxis=dict(title='measurement'),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)
plot(fig)