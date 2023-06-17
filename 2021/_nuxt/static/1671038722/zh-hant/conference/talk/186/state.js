window.__NUXT__=(function(a,b,c){return {staticAssetsBase:"\u002F2021\u002F_nuxt\u002Fstatic\u002F1671038722",layout:"default",error:b,state:{sponsorsData:[],jobsData:[],schedulesData:[],keynotesData:[],youtubeInfo:[],speechesData:[],speechData:{id:186,begin_time:"2021-10-03T05:00:00Z",end_time:"2021-10-03T05:45:00Z",is_remote:false,location:"6-r2",youtube_id:"5bIJ1SwF2bk",title:"從 Flask 邁向 FastAPI 的心路歷程 - 用房屋估價模型服務體驗急速開發、高效能的快感!",category:"WEB",language:"ZHZH",python_level:"INTERMEDIATE",recording_policy:c,abstract:"過往在使用Python開發API的時候，基於WSGI架構下，運算中遇到IO bound時，可以透過多線程去處理，但遇到cpu bound時，多線程並不是一個好的選擇，因為線程會受限於GIL，並不會有效提升效能，而當遇到運算請求量較大時，為了因應大量的運算請求，可以透過多進程來彌補多線程的不足，但同時也需要承擔過多的資源消耗以及考慮Inter-Process Communication overhead。\r\n\r\n而這些問題在FastAPI得到了救贖，FastAPI是一個建立在ASGI架構下的Web框架，以Python所提出的非同步概念為基礎，透過Coroutine的方式，去提高CPU運算效率，去改善多線程、多進程對於cpu bound遇到的問題。\r\n  \r\n本次演講主要透過房屋估價模型服務程式碼的解說，分享如何從過去使用的Flask框架，轉換為FastAPI框架。透過非同步的設計，即使有GIL的限制，仍舊能夠透過單線程去達到類似多進程的運算效能，減少開啟多進程造成的資源耗費過多。此外，透過程式碼，說明這兩個框架開發上的不同之處，以及轉換過程中曾經遇到的問題，讓想使用FastAPI但還在觀望的人能夠有參考方向，減少未來使用時踩雷的機會!",detailed_description:"### 想透過本次演講告訴大家的內容\r\n- ASGI架構是什麼?FastAPI是什麼?是如何應用Async?\r\n- 藉由實際痛點(mutli-thread、mutli-process issue)案例-房屋估價模型服務分析Flask與FastAPI開發上相異之處，以及這樣的相異之處對開發上的影響\r\n- 非同步框架帶來好處的同時，使用上所需的注意事項\r\n- 實際房屋估價模型服務轉換前轉後的數據比較\r\n- 除了效能以外，FastAPI所帶來的好處\r\n- 轉換上的心路歷程\r\n\r\n### 本次使用的相關工具\r\n- FastAPI\r\n- Flask",slide_link:a,slido_embed_link:"https:\u002F\u002Fapp.sli.do\u002Fevent\u002Flypoclvj",hackmd_embed_link:"https:\u002F\u002Fhackmd.io\u002F@pycontw\u002Frk6Kg4cfY\u002Fedit",speakers:[{thumbnail_url:"https:\u002F\u002Ftw.pycon.org\u002Ftemp\u002Fmedia\u002Fcache\u002F92\u002F97\u002F9297bc672d1d64bb5b16598e7662be6e.jpg",name:"陳家丞",github_profile_url:a,twitter_profile_url:a,facebook_profile_url:a,bio:"Intelligent System Engineer at E.SUN Bank.\r\nLike to study python Web Framework, e.g., Flask、FastAPI."}],event_type:"talk"},i18n:{routeParams:{}}},serverRendered:c,routePath:"\u002Fzh-hant\u002Fconference\u002Ftalk\u002F186",config:{gtm:{id:void 0},_app:{basePath:"\u002F2021\u002F",assetsPath:"\u002F2021\u002F_nuxt\u002F",cdnURL:b}}}}("",null,true));