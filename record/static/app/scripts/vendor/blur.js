var CanvasImage=function(e,t)
{
	this.image=t,
	this.element=e,
	this.element.width=this.image.width,
	this.element.height=this.image.height;
	var n=navigator.userAgent.toLowerCase().indexOf("chrome")>-1,
	r=navigator.appVersion.indexOf("Mac")>-1;
	n&&r&&(this.element.width=Math.min(this.element.width,300),this.element.height=Math.min(this.element.height,200)),
	this.context=this.element.getContext("2d"),
	this.context.drawImage(this.image,0,0)
};
CanvasImage.prototype={
	blur:function(e){
		this.context.globalAlpha=.5;
		for(var t=-e;t<=e;t+=2)
			for(var n=-e;n<=e;n+=2)
				this.context.drawImage(this.element,n,t),
			n>=0&&t>=0&&this.context.drawImage(this.element,-(n-1),-(t-1));
			this.context.globalAlpha=1
		}
},

$(function(){
	var image,canvasImage,canvas;
	$(".blur").each(function(){
		canvas=this,
		image=new Image,
		image.onload=function(){
			canvasImage=new CanvasImage(canvas,this),
			canvasImage.blur(4)
		},
		image.src=$(this).attr("src");
	});
});
