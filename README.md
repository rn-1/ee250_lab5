# Lab 5

## Team Members

- Vishnu Kadaba
- Ryan Nene

## Lab Question Answers

Answer for Question 1:
dBm stands for decibel-milliwatt, and is used to describe the signal strength of a wifi signal.
between -50 to -70 dBm is considered good, below -80 to -90dbm is considered bad

Answer for Question 2:
the actual command/directories used by each os will be different, hence we need a different command. Whatever is returned/printed is also different

Answer for Question 3:
runs the passed commands and takes its output. essentially just runs the command in a new thread, and then pipes its output into a variable.

Answer for Question 4:
searches a string based on given regex, returns a matching substring from the string.

Answer for Question 5:
we want dbm, but the units weren't originally in dbm
windows reports a percentage.

Answer for Question 6:
Measures variability/spread in data
Higher std dev = more variation in signal strength
Useful to understand stability of WiFi signal at each location
Helps identify locations with inconsistent signal

Answer for Question 7:
2D labeled data structure
Like spreadsheet/SQL table
Benefits:
Easy data manipulation
Built-in statistical functions
Simple integration with plotting libraries
Clean data organization

Answer for Question 8:
Show uncertainty/variation in measurements
Length = 1 standard deviation up/down
Important because:
Indicates signal stability
Shows measurement reliability
Helps compare locations statistically

Answer for Question 9:
Signal strength typically:
Decreases with distance from router
Weakens through walls/floors
Affected by:
Building materials
Electronic interference
Physical obstacles
Router placement

# Part 2

1. How does distance affect TCP and UDP throughput?
   TCP and UDP throughput decrease with distance, but TCP degrades more gradually while UDP drops sharply without packet recovery.

2. At what distance does significant packet loss occur for UDP? based on plot
   Significant UDP packet loss typically begins at 8 meters from the Pi.

3. Why does UDP experience more packet loss than TCP?
   UDP experiences more packet loss than TCP because it lacks reliability like acknowledgments and retransmissions.

4. What happens if we increase the UDP bandwidth (-b 100M)?
   Increasing UDP bandwidth to 100M leads to higher packet loss, potentially resulting in decreased actual throughput.

5. Would performance be different on 5 GHz Wi-Fi vs. 2.4 GHz?
   5 GHz offers higher throughput, less interference, and shorter range. 2.4 GHz provides better ranges but lower maximum throughput.
