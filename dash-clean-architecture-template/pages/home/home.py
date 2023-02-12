import dash_html_components as html
import input_svrp_v3.main as ip

input_data = ip.seed()

layout = html.Div(html.P("This is the content of the Home page!"))

