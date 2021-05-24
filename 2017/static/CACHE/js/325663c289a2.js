(function(){if(!NodeList.prototype.forEach){NodeList.prototype.forEach=function(cb,scope){let i=0
while(i<this.length){if(i in this){cb.call(scope,this[i],i,this)}
i++}}}})();document.querySelectorAll('.control-nav > .lang > nav > a, .header-menu-nav > a').forEach((el)=>{el.addEventListener('click',function(e){e.preventDefault();var form=document.getElementById('nav-lang-form');form.next.value=this.getAttribute('href');form.language.value=this.getAttribute('data-lang');form.submit();});});(function(){const controlRootEl=()=>{if($('body').hasClass('show-menu')){$('html').css({overflow:'hidden',position:'fixed'});}else{$('html').css({overflow:'auto',position:'relative'});}};$('.btn-menu').on('click',(e)=>{e.preventDefault();$('body').toggleClass('show-menu');controlRootEl();});$('.header-nav > .parent > a:first-child').on('click',(e)=>{e.preventDefault();$(e.target).parent().toggleClass('expanded');});$('.btn-show-lang-menu').on('click',(e)=>{$('.header-nav').hide();$('.header-menu-nav').show();});$('.btn-back-to-menu').on('click',(e)=>{$('.header-nav').show();$('.header-menu-nav').hide();});$('.btn-close').on('click',(e)=>{$('body').removeClass('show-menu');controlRootEl();});window.addEventListener('resize',()=>{if(window.innerWidth<=599){$('.header-nav').show();$('.header-menu-nav').hide();}else{$('body').removeClass('show-menu');}});})();(function(){function smoothScroll(el,to,duration){if(duration<0){return}
var difference=to-$(window).scrollTop()
var perTick=difference/duration*10
this.scrollToTimerCache=setTimeout(function(){if(!isNaN(parseInt(perTick,10))){window.scrollTo(0,$(window).scrollTop()+perTick)
smoothScroll(el,to,duration-10)}}.bind(this),10)}
function scrollTo(target){smoothScroll($(window),$(target).offset().top,200)
if(window.history&&window.history.pushState){if(target!==window.location.hash){window.history.pushState('','',window.location.pathname+window.location.search+target)}}}
$('.quick-jump-link').on('click',function(e){e.preventDefault()
scrollTo($(e.currentTarget).attr('href'))})
$('.back-to-top').on('click',function(e){e.preventDefault()
smoothScroll($(window),0,200)
if(window.history&&window.history.pushState){if(window.location.hash!==''){window.history.pushState('','',window.location.pathname+window.location.search)}}})
function padZero(number,digits){let s=number
while(s.length<digits){s='0'+s}
return s}
const today=new Date()
const todayId=[padZero(today.getFullYear(),4),padZero(today.getMonth()+1,2),padZero(today.getDate(),2),].join('-')
if($(todayId).length>0){scrollTo(todayId,200)}})();