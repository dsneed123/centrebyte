//////  INIT  ////////
function startAd() {
	hideElement(txt_1);
	hideElement(txt_1b);
	hideElement(txt_2);
	hideElement(cta);
	hideElement(logo);
	hideElement(orangeBckgrd);
	hideElement(icon);
	hideElement(shimmer);

  	addListeners();
	TweenMax.set(".lgArt",{transformOrigin: "left top", scale:.5});
  	TweenMax.delayedCall(0,intro);
}

//////  START ANIMATION  ////////

intro = function() {  
	TweenMax.delayedCall(0.1,revealAd);
	TweenMax.delayedCall(0.6,scene1);
	TweenMax.delayedCall(5,ender);
}

revealAd = function() { 

	TweenMax.to(cover,.5,{alpha: 0});
}

scene1 = function() { 
	showElement(txt_1);
	showElement(txt_1b);
	showElement(txt_2);
	
	showElement(orangeBckgrd);
	showElement(cta);
	showElement(logo);
	showElement(icon);
	
	TweenMax.from(orangeBckgrd,.5,{ y:-150, ease:Power2.easeInOut, delay:.2});
	
	TweenMax.from(cta,.5,{ y:12, alpha:0, ease:Power2.easeInOut, delay:.8});
	TweenMax.from(logo,.5,{ y:12, alpha:0, ease:Power2.easeInOut, delay:.6});
	
	TweenMax.from(txt_1,.5,{ y:12, alpha:0, ease:Power2.easeInOut, delay:.4, });
	TweenMax.from(txt_1b,.5,{ y:12, alpha:0, ease:Power2.easeInOut, delay:.4});
	TweenMax.from(txt_2,.5,{ y:12, alpha:0, ease:Power2.easeInOut, delay:3});
	
	TweenMax.to(iconImg, .5, { x:8, scale: 1,   transformOrigin: "50% 40%", ease: Back.easeOut.config(4),  delay: 2});
}

ender = function() {
	showElement(shimmer);

	lightPass(); 
	TweenMax.delayedCall(2,lightPass);
}


lightPass = function() {
	TweenMax.set(shimmer,{left:-250});
	TweenMax.to(shimmer,1.5,{left:350, rotation:0.01});
}

addListeners = function() {
  rolloverCatch.addEventListener('mouseover', lightPass, false);
  
}


showElement = function(e){
  e.style.visibility = 'visible';
}

hideElement = function(e){
  e.style.visibility = 'hidden';
}