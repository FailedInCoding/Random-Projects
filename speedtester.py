import speedtest

st = speedtest.Speedtest()

print('1) Download Speed: ',end='')
print(st.download())

print('1) UpLoad Speed: ', end='')
print(st.upload())

print('1) Ping: ', end='')
servernames = []
st.get_servers(servernames)
print(st.results.ping)