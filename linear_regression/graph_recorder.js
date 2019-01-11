window.onload = function () {
    const canvas = document.getElementById("graph");
    const ctx = canvas.getContext("2d");

    const {left, top} = canvas.getBoundingClientRect();

    let points = [];

    document.getElementById('graph').onclick = e => {
      ctx.strokeRect(e.x-left,e.y-top,5,5);
      points.push({x: e.x-left,y: e.y-top});
      console.log("x: " + e.x,"y: " + e.y,"left -> " + left,"top -> " + top);
      drawLine(points);
    };
};

const drawLine = (points) => {
  console.log(points);
  let sumX = 0, sumY = 0;
  points.forEach(point => {
    sumX += point.x;
    sumY += point.y;
  });
  const meanX = sumX/points.length;
  const meanY = sumY/points.length;
  console.log(meanX, meanY);
};

// var c = document.getElementById("myCanvas");
// var ctx = c.getContext("2d");
// ctx.beginPath();
// ctx.moveTo(0, 0);
// ctx.lineTo(300, 150);
// ctx.stroke();
