(function(g){var window=this;'use strict';var C6=function(a){g.W.call(this,{G:"div",L:"ytp-miniplayer-ui"});this.pe=!1;this.player=a;this.T(a,"minimized",this.yg);this.T(a,"onStateChange",this.IG)},D6=function(a){g.GM.call(this,a);
this.i=new C6(this.player);this.i.hide();g.tM(this.player,this.i.element,4);a.Le()&&(this.load(),g.M(a.getRootNode(),"ytp-player-minimized",!0))};
g.w(C6,g.W);g.k=C6.prototype;
g.k.CE=function(){this.tooltip=new g.hQ(this.player,this);g.H(this,this.tooltip);g.tM(this.player,this.tooltip.element,4);this.tooltip.scale=.6;this.wc=new g.zN(this.player);g.H(this,this.wc);this.Dg=new g.W({G:"div",L:"ytp-miniplayer-scrim"});g.H(this,this.Dg);this.Dg.Ea(this.element);this.T(this.Dg.element,"click",this.qA);var a=new g.W({G:"button",Ha:["ytp-miniplayer-close-button","ytp-button"],W:{"aria-label":"Close"},U:[g.xK()]});g.H(this,a);a.Ea(this.Dg.element);this.T(a.element,"click",this.Hi);
a=new g.Q1(this.player,this);g.H(this,a);a.Ea(this.Dg.element);this.Bp=new g.W({G:"div",L:"ytp-miniplayer-controls"});g.H(this,this.Bp);this.Bp.Ea(this.Dg.element);this.T(this.Bp.element,"click",this.qA);var b=new g.W({G:"div",L:"ytp-miniplayer-button-container"});g.H(this,b);b.Ea(this.Bp.element);a=new g.W({G:"div",L:"ytp-miniplayer-play-button-container"});g.H(this,a);a.Ea(this.Bp.element);var c=new g.W({G:"div",L:"ytp-miniplayer-button-container"});g.H(this,c);c.Ea(this.Bp.element);this.qN=new g.ZO(this.player,
this,!1);g.H(this,this.qN);this.qN.Ea(b.element);b=new g.XO(this.player,this);g.H(this,b);b.Ea(a.element);this.nextButton=new g.ZO(this.player,this,!0);g.H(this,this.nextButton);this.nextButton.Ea(c.element);this.Gg=new g.TP(this.player,this);g.H(this,this.Gg);this.Gg.Ea(this.Dg.element);this.Hc=new g.fP(this.player,this);g.H(this,this.Hc);g.tM(this.player,this.Hc.element,4);this.fA=new g.W({G:"div",L:"ytp-miniplayer-buttons"});g.H(this,this.fA);g.tM(this.player,this.fA.element,4);a=new g.W({G:"button",
Ha:["ytp-miniplayer-close-button","ytp-button"],W:{"aria-label":"Close"},U:[g.xK()]});g.H(this,a);a.Ea(this.fA.element);this.T(a.element,"click",this.Hi);a=new g.W({G:"button",Ha:["ytp-miniplayer-replay-button","ytp-button"],W:{"aria-label":"Close"},U:[g.CK()]});g.H(this,a);a.Ea(this.fA.element);this.T(a.element,"click",this.HV);this.T(this.player,"presentingplayerstatechange",this.Nc);this.T(this.player,"appresize",this.xb);this.T(this.player,"fullscreentoggled",this.xb);this.xb()};
g.k.show=function(){this.Ld=new g.Dr(this.qq,null,this);this.Ld.start();this.pe||(this.CE(),this.pe=!0);0!==this.player.getPlayerState()&&g.W.prototype.show.call(this);this.Hc.show();this.player.unloadModule("annotations_module")};
g.k.hide=function(){this.Ld&&(this.Ld.dispose(),this.Ld=void 0);g.W.prototype.hide.call(this);this.player.Le()||(this.pe&&this.Hc.hide(),this.player.loadModule("annotations_module"))};
g.k.ya=function(){this.Ld&&(this.Ld.dispose(),this.Ld=void 0);g.W.prototype.ya.call(this)};
g.k.Hi=function(){this.player.stopVideo();this.player.Oa("onCloseMiniplayer")};
g.k.HV=function(){this.player.playVideo()};
g.k.qA=function(a){if(a.target===this.Dg.element||a.target===this.Bp.element)this.player.V().N("kevlar_miniplayer_play_pause_on_scrim")?g.AJ(this.player.zb())?this.player.pauseVideo():this.player.playVideo():this.player.Oa("onExpandMiniplayer")};
g.k.yg=function(){g.M(this.player.getRootNode(),"ytp-player-minimized",this.player.Le())};
g.k.rd=function(){this.Hc.Xb();this.Gg.Xb()};
g.k.qq=function(){this.rd();this.Ld&&this.Ld.start()};
g.k.Nc=function(a){g.T(a.state,32)&&this.tooltip.hide()};
g.k.xb=function(){g.sP(this.Hc,0,this.player.eb().getPlayerSize().width,!1);g.gP(this.Hc)};
g.k.IG=function(a){this.player.Le()&&(0===a?this.hide():this.show())};
g.k.jc=function(){return this.tooltip};
g.k.Te=function(){return!1};
g.k.vf=function(){return!1};
g.k.Ai=function(){return!1};
g.k.dB=function(){};
g.k.vn=function(){};
g.k.qs=function(){};
g.k.Kn=function(){return null};
g.k.sj=function(){return new g.Cm(0,0,0,0)};
g.k.handleGlobalKeyDown=function(){return!1};
g.k.handleGlobalKeyUp=function(){return!1};
g.k.zq=function(a,b,c,d,e){var f=0,h=d=0,l=g.Vm(a);if(b){c=g.Or(b,"ytp-prev-button")||g.Or(b,"ytp-next-button");var m=g.Or(b,"ytp-play-button"),n=g.Or(b,"ytp-miniplayer-expand-watch-page-button");c?f=h=12:m?(b=g.Tm(b,this.element),h=b.x,f=b.y-12):n&&(h=g.Or(b,"ytp-miniplayer-button-top-left"),f=g.Tm(b,this.element),b=g.Vm(b),h?(h=8,f=f.y+40):(h=f.x-l.width+b.width,f=f.y-20))}else h=c-l.width/2,d=25+(e||0);b=this.player.eb().getPlayerSize().width;e=f+(e||0);l=g.rg(h,0,b-l.width);e?(a.style.top=e+"px",
a.style.bottom=""):(a.style.top="",a.style.bottom=d+"px");a.style.left=l+"px"};
g.k.showControls=function(){};
g.k.fl=function(){};
g.k.Dk=function(){return!1};g.w(D6,g.GM);D6.prototype.create=function(){};
D6.prototype.Ri=function(){return!1};
D6.prototype.load=function(){this.player.hideControls();this.i.show()};
D6.prototype.unload=function(){this.player.showControls();this.i.hide()};g.FM("miniplayer",D6);})(_yt_player);
