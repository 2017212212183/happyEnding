$("#good").click(function(e){
    let ev= ev || window.event;
    let mousePos = mouseCoords(ev);
    //alert(ev.pageX);
    makearc(mousePos.x,mousePos.y,GetRandomNum(10,50),0,180,'red');
})