import matplotlib.pyplot as plt
import pandas as pd


tcp2 = pd.read_csv("/Users/ryan/Desktop/EE250_SHARED/lab5-Demo/iperf_tcp_2m.csv")
tcp4 = pd.read_csv("/Users/ryan/Desktop/EE250_SHARED/lab5-Demo/iperf_tcp_4m.csv")
tcp6 = pd.read_csv("/Users/ryan/Desktop/EE250_SHARED/lab5-Demo/iperf_tcp_6m.csv")
tcp8 = pd.read_csv("/Users/ryan/Desktop/EE250_SHARED/lab5-Demo/iperf_tcp_8m.csv")
tcp10 = pd.read_csv("/Users/ryan/Desktop/EE250_SHARED/lab5-Demo/iperf_tcp_10m.csv")

udpruns = []

print(tcp2)

for num in range(2,11,2):
    exec(f"udp{num} = pd.read_csv(\"/Users/ryan/Desktop/EE250_SHARED/lab5-Demo/iperf_udp_{num}m.csv\")")
    exec (f"udpruns.append(udp{num})")


tcpruns = [tcp2,tcp4,tcp6,tcp8,tcp10]


avg_rate = [t['Avg'] for t in tcpruns]


# plt.plot(tcp2[], list(range(2,11,2)))
# plt.show()