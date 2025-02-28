import matplotlib.pyplot as plt
import pandas as pd


tcp2 = pd.read_csv("/Users/vishnu/Desktop/EE250/ee250_lab5/iperf_tcp_2m.csv")
tcp4 = pd.read_csv("/Users/vishnu/Desktop/EE250/ee250_lab5/iperf_tcp_4m.csv")
tcp6 = pd.read_csv("/Users/vishnu/Desktop/EE250/ee250_lab5/iperf_tcp_6m.csv")
tcp8 = pd.read_csv("/Users/vishnu/Desktop/EE250/ee250_lab5/iperf_tcp_8m.csv")
tcp10 = pd.read_csv("/Users/vishnu/Desktop/EE250/ee250_lab5/iperf_tcp_10m.csv")

udpruns = []

print(tcp4)
print(tcp4.columns)

for num in range(2, 11, 2):
    exec(
        f'udp{num} = pd.read_csv("/Users/vishnu/Desktop/EE250/ee250_lab5/iperf_udp_{num}m.csv")'
    )
    exec(f"udpruns.append(udp{num})")


tcpruns = [tcp2, tcp4, tcp6, tcp8, tcp10]


avg_rate = [t[" Avg"] for t in tcpruns]

for i in range(5):
    tcpvals = []
    udpvals = []
    for x in range(5):
        exec(f"tcpvals.append(tcpruns[{i}][' Run{x+1}'])")
        exec(f"udpvals.append(udpruns[{i}][' Run{x+1}'])")
    print("here", tcpvals)
    print("here2", udpvals)
    plt.plot(list(range(1, 6)), tcpvals, label=f"TCP {i*2+2}M")
    plt.plot(list(range(1, 6)), udpvals, label=f"UDP {i*2+2}M")
    plt.legend()
    plt.show()

    plt.savefig(f"TCP_vs_UDP_{i*2+2}m.jpg")
    # plt.close()  # Close the figure to free memory

# plt.show()
