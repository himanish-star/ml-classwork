window.onload = function () {
  const canvas = document.getElementById("graph");
  const canvas2 = document.getElementById("graph2");
  const ctx = canvas.getContext("2d");
  const ctx2 = canvas2.getContext("2d");

  const {left, top, width, height} = canvas.getBoundingClientRect();
  const {left: left2, top: top2, width: width2, height: height2} = canvas2.getBoundingClientRect();

  console.log(canvas2.getBoundingClientRect());

  let points = [];

  document.getElementById('graph').onclick = e => {
    clearCanvas(ctx,width,height);
    points.push({x: e.x-left,y: e.y-top});
    plotPoints(ctx,points);
    if(points.length > 1) {
      const {beta0,beta1} = drawLine(points,left+width,top+height);
      const newPoints = residualPlot(ctx2,points,beta0,beta1);
      console.log(newPoints);
      plotResidualPoints(ctx2,newPoints,left2,top2,width2,height2);
    }
  };

  // window.setTimeout(() => {
  //   clearCanvas(ctx,width,height);
  // },2000);

};

const plotResidualPoints = (ctx,newPoints,left,top,width,height) => {
  ctx.clearRect(0,0,width,height);
  newPoints.forEach(point => {
    ctx.strokeRect(point.yexp/2,height/2+point.yexp/2-point.yact/2,5,5);
    console.log(point.yexp,point.yexp-point.yact);
  });
};

const plotPoints = (ctx,points) => {
  points.forEach(point => {
    ctx.strokeRect(point.x,point.y,5,5);
  });
};

const clearCanvas = (ctx,width,height) => {
  ctx.clearRect(0,0,width,height);
};

const residualPlot = (ctx,points,beta0,beta1) => {
  let newPoints = [];
  points.forEach(point => {
    const yExpected = point.y;
    const yActual = beta0 + (beta1*point.x);
    newPoints.push({yexp: yExpected,yact: yActual});
  });
  return newPoints;
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
  return {beta0,beta1};
};
