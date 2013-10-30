set multiplot
plot "plan.png" binary filetype=png w rgbimage
set xrange [-200:1800]
set yrange [-200:1200]
plot "purplePlot.dat" using 1:2 pt 7 ps 2 lc rgb "#CB00F5"
reread
unset multiplot
pause 100

