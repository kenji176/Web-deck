
function showClock() {
    let nowTime = new Date();
    let nowHour = nowTime.getHours();
    let nowMin  = nowTime.getMinutes();
    if (nowMin.toString().length == 1){
        nowMin = '0'+nowMin;
    }else{;}
    let msg = nowHour + ":"+nowMin;
    document.getElementById("time").innerHTML = msg;
}
setInterval('showClock()',1000);