import os

#those variables are defined in system variable
#.bash_profile
#需要重启pycharm才会生效，即使你在shell export了也是无效的
print(os.environ['JOINT_QUANT_USERNAME'])
print(os.environ['JOINT_QUANT_PWD'])

# init plotly
import plotly
plotly.tools.set_credentials_file(username='XXX', api_key='XXX')


