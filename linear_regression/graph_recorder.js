window.onload = function () {
    const canvas = document.getElementById("graph");
    const ctx = canvas.getContext("2d");

    const {left, top} = canvas.getBoundingClientRect();

    document.getElementById('graph').onclick = e => {
      ctx.strokeRect(e.x-left,e.y-top,1,1);
      console.log("x: " + e.x,"y: " + e.y,"left -> " + left,"top -> " + top);
    };
};
