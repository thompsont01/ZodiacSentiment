
/*
data = [ [ sign , yesterday sentiment , today sentiment ]]
for sign in signs:
    if today > yesterday:
        set sign id to visible
    else:
        set to invisible
last update = ()
***add server script for twitter listener & sentiment updater
*/
d3.csv("timestamped_summary.csv", function(data){
    console.log(data)
});
