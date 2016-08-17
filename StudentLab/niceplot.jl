using PyCall
@pyimport matplotlib as mpl
mpl.use("pdf")
import PyPlot; const plt = PyPlot
using LaTeXStrings

#plt.rc("font", family="serif", serif="Times")

plt.rc("text",usetex=true)
plt.rc("xtick",labelsize=10)
plt.rc("ytick",labelsize=10)
plt.rc("axes",labelsize=10)

width = 3.487
height = width / 1.618

fig, ax = plt.subplots()
fig[:subplots_adjust](left=.15, bottom=.19, right=0.97, top=.97)

x = 0:0.1:3
plt.plot(x,sin(x))

#\mathrm{\alpha}
plt.ylabel("Some text "*L"\int\alpha \mathrm{d}x")
plt.xlabel("another metric")

fig[:set_size_inches](width,height)
plt.grid("off")

fig[:savefig]("plot2.pdf")
