/* Tek dokunuşta güvenli şehir rotası. Binalar, ağaçlar ve çeşme korunur. */
(function () {
  'use strict';
  function blocked(x,z,colliders,radius) {
    if(x < -59 || x > 59 || z < -116 || z > 35) return true;
    return colliders.some(c => c.c ? Math.hypot(x-c.x,z-c.z)<c.r+radius :
      Math.hypot(x-Math.max(c.x0,Math.min(c.x1,x)),z-Math.max(c.z0,Math.min(c.z1,z)))<radius);
  }
  function path(start,goal,colliders,radius,reach) {
    radius=radius || 1; reach=reach || 1.4;
    const step=1.5,width=80,height=102,point=i=>({x:-59+i%width*step,z:-116+Math.floor(i/width)*step});
    const clear=(a,b)=>{const n=Math.max(1,Math.ceil(Math.hypot(b.x-a.x,b.z-a.z)/.4));for(let i=0;i<=n;i++){const t=i/n;if(blocked(a.x+(b.x-a.x)*t,a.z+(b.z-a.z)*t,colliders,radius))return false;}return true;};
    let first=-1,best=Infinity;
    for(let i=0;i<width*height;i++){const p=point(i),d=Math.hypot(p.x-start.x,p.z-start.z);if(d<best&&d<3&&!blocked(p.x,p.z,colliders,radius)&&clear(start,p)){first=i;best=d;}}
    if(first<0)return [];
    const parents=new Int32Array(width*height).fill(-1),seen=new Uint8Array(width*height),queue=[first];seen[first]=1;let end=-1;
    for(let k=0;k<queue.length;k++){const i=queue[k],a=point(i);if(Math.hypot(a.x-goal.x,a.z-goal.z)<reach){end=i;break;}const x=i%width,z=Math.floor(i/width);
      for(let dx=-1;dx<=1;dx++)for(let dz=-1;dz<=1;dz++){if((!dx&&!dz)||x+dx<0||x+dx>=width||z+dz<0||z+dz>=height)continue;const j=(z+dz)*width+x+dx,b=point(j);if(seen[j]||blocked(b.x,b.z,colliders,radius)||!clear(a,b))continue;parents[j]=i;seen[j]=1;queue.push(j);}}
    if(end<0)return [];
    const raw=[];for(let i=end;i>=0;i=parents[i])raw.push(point(i));raw.reverse();
    const out=[];let anchor=start;
    for(let i=0;i<raw.length;){let j=i;while(j+1<raw.length&&clear(anchor,raw[j+1]))j++;out.push(raw[j]);anchor=raw[j];i=j+1;}
    return out;
  }
  function touches(a,b,target,radius) {
    const dx=b.x-a.x,dz=b.z-a.z,len=dx*dx+dz*dz;
    const t=len?Math.max(0,Math.min(1,((target.x-a.x)*dx+(target.z-a.z)*dz)/len)):0;
    return Math.hypot(target.x-a.x-t*dx,target.z-a.z-t*dz)<radius;
  }
  window.UNICORN_NAVIGATION=Object.freeze({path,blocked,touches});
}());
