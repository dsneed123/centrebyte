//////  INIT  ////////
function startAd() {
	hideElement(txt_1);
	hideElement(txt_3);
	hideElement(logo);
	hideElement(orangeBckgrd);
	hideElement(icon);
	hideElement(whiteChev);
	hideElement(blackChev);
	hideElement(shimmer);

  	addListeners();
	TweenMax.set(".lgArt",{transformOrigin: "left top", scale:.5});
  	TweenMax.delayedCall(0,intro);
}

//////  START ANIMATION  ////////

intro = function() {  
	TweenMax.delayedCall(0.1,revealAd);
	TweenMax.delayedCall(0.6,scene1);
	TweenMax.delayedCall(5.5,scene2);
	TweenMax.delayedCall(8,ender);
}

revealAd = function() { 

	TweenMax.to(cover,.5,{alpha: 0});
}

scene1 = function() { 
	showElement(txt_1);
	showElement(blackChev);
	showElement(orangeBckgrd);
	showElement(icon);
	
	TweenMax.from(orangeBckgrd,.5,{ x:-728, ease:Power2.easeInOut, delay:.2});
	TweenMax.from(blackChev,.1,{ x:12, alpha:0, ease:Power2.easeInOut, delay:.6});
	TweenMax.from(txt_1,.5,{ y:12, alpha:0, ease:Power2.easeInOut, delay:.4});
	TweenMax.to(iconImg, .5, { x:40, scale: 1,   transformOrigin: "20% 90%", ease: Back.easeOut.config(4),  delay: 2});
}

scene2 = function() { 
	showElement(txt_3);
	showElement(whiteChev);
	
	showElement(logo);
	
	TweenMax.to(txt_1,.1,{ y:-12,  alpha:0, ease:Power2.easeInOut, delay:0});
	TweenMax.to(orangeBckgrd,.4,{ x:703, ease:Power2.easeInOut, delay:0});
	TweenMax.to(blackChev,.1,{ alpha:0, ease:Power2.easeInOut, delay:.2});
	TweenMax.to(iconImg, .1, { alpha:0,  delay: 0});
	
	TweenMax.from(logo,.5,{ y:12, alpha:0, ease:Power2.easeInOut, delay:.3});
	TweenMax.from(txt_3,.5,{ y:12, alpha:0, ease:Power2.easeInOut, delay:.5});
	TweenMax.from(whiteChev,.1,{ alpha:0, ease:Power2.easeInOut, delay:.3});
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