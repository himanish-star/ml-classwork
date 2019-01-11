window.onload = function () {
    const canvas = document.getElementById("graph");
    const ctx = canvas.getContext("2d");

    const {left, top, width, height} = canvas.getBoundingClientRect();

    let points = [];

    document.getElementById('graph').onclick = e => {
      ctx.strokeRect(e.x-left,e.y-top,5,5);
      points.push({x: e.x-left,y: e.y-top});
      drawLine(points,left+width,top+height);
    };
};

const drawLine = (points,endBottom,endRight) => {
  let sumX = 0, sumY = 0;
  let summation_xy = 0, summation_x2 = 0;
  points.forEach(point => {
    sumX += point.x;
    sumY += point.y;
    summation_xy += point.x * point.y;
    summation_x2 += point.x * point.x;
  });
  const meanX = sumX/points.length;
  const meanY = sumY/points.length;

  const beta1 = (summation_xy - (points.length*meanX*meanY))/(summation_x2 - (points.length*meanX*meanX));
  const beta0 = meanY - (beta1*meanX);

  let c = document.getElementById("graph");
  let newX,newY;
  let ctx = c.getContext("2d");
  ctx.beginPath();
  ctx.moveTo(meanX,meanY);
  newX=-beta0/beta1;
  newY=beta0;
  ctx.lineTo(0, newY);
  ctx.moveTo(meanX,meanY);
  ctx.lineTo(newX, 0);
  ctx.moveTo(meanX,meanY);
  newX=(endBottom-beta0)/beta1;
  newY=beta0+(beta1*endRight);
  ctx.lineTo(endRight, newY);
  ctx.moveTo(meanX,meanY);
  ctx.lineTo(newX, endBottom);
  ctx.stroke();
};
