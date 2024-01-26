window.__NUXT__=(function(a,b,c,d){return {staticAssetsBase:"\u002F2023\u002F_nuxt\u002Fstatic\u002F1706235397",layout:"default",error:d,state:{sponsorsData:[],jobsData:[],schedulesData:[],keynotesData:[],youtubeInfo:[],speechesData:[],speechData:{id:290,begin_time:"2023-09-03T02:40:00Z",end_time:"2023-09-03T03:25:00Z",is_remote:b,location:"5-r1",youtube_id:c,title:"在 Dcard 我們如何用 Python 打造推薦系統",category:"ML",language:"ZHEN",python_level:"INTERMEDIATE",recording_policy:a,abstract:"At our Dcard ML team, we rely on Python to create our recommendation system. In addition to the data science and modeling stages, we also use Python to build the program responsible for handling requests in real-world usage. To ensure our program's robustness, we incorporate various features of the Python ecosystem, such as abstract classes, in multiple areas. Today, we are excited to share how we utilize these features at different stages of the ML lifecycle. We'll also discuss any challenges we encountered and how we overcame them, as well as any best practices we learned along the way.",detailed_description:"* 我預計在這次投稿中提到在 Dcard 我們怎麼使用 Python 來做 ML Lifecycle 中的 Modeling & Serving 環節。在普遍的 ML Lifecycle 中包含了 problem framing, dataset preparation, modeling, serving 等階段。為了完整性我會在 introduction 的地方簡單提到一下各個階段的主要目標，接著將較多時間花在我們如何用 python 撰寫穩定、可讀性高，並且利於重用的程式碼。\r\n* 在 modeling 的部分我預計會提到我們如何迭代的開發模型。主要是建立在使用 abstract class 建立模型的接口，利用 scikit-learn pipeline 封裝並確保 train\u002Fserving 時的 data transformation 一致，並將模型訓練時的參數以 configuration as code 的概念，利用 dataclass 包裝起來並進行版本控制。\r\n* 在 serving 的部分則是會提到我們在 serving 的時候同樣是利用了大量的 abstract class 來定義不同 ranking, database 相關的接口，以及我們如何使用 numpy array 取代 pandas dataframe 以達到加速的效果\r\n* reference\r\n    * ML lifecycle: https:\u002F\u002Fhuyenchip.com\u002Fmachine-learning-systems-design\u002Fdesign-a-machine-learning-system.html\r\n    * abstract class: https:\u002F\u002Fdocs.python.org\u002F3\u002Flibrary\u002Fabc.html\r\n    * dataclasses: https:\u002F\u002Fdocs.python.org\u002F3\u002Flibrary\u002Fdataclasses.html\r\n    * scikit-learn pipeline: https:\u002F\u002Fscikit-learn.org\u002Fstable\u002Fmodules\u002Fgenerated\u002Fsklearn.pipeline.Pipeline.html\r\n    * numpy array: https:\u002F\u002Fnumpy.org\u002Fdoc\u002Fstable\u002Freference\u002Fgenerated\u002Fnumpy.array.html",slide_link:"https:\u002F\u002Fdrive.google.com\u002Ffile\u002Fd\u002F1TRHSuSLWHQNOj8E8RuZ58RiTnNj1sXwv\u002Fview?usp=sharing",slido_embed_link:"https:\u002F\u002Fapp.sli.do\u002Fevent\u002FqDmLwJDxPbvDLgmAWKZD86",hackmd_embed_link:"https:\u002F\u002Fhackmd.io\u002F@pycontw\u002FH1XDUoQ6h",speakers:[{thumbnail_url:"https:\u002F\u002Ftw.pycon.org\u002Fprs\u002Fmedia\u002Fcache\u002F69\u002F75\u002F69754f87f5e09e112a005cd90fdd1443.jpg",name:"陳子元",github_profile_url:"https:\u002F\u002Fgithub.com\u002Fzychen423",twitter_profile_url:c,facebook_profile_url:c,bio:"我是陳子元，現職為 Dcard 的機器學習工程師。一開始以為自己想做研究，曾在中研院的自然語言處理實驗室擔任研究助理，後來發現當工程師還是比較有趣於是成為了一個機器學習工程師，對自然語言處理、推薦系統以及資料工程都有興趣。"}],event_type:"talk"},relatedData:[],configs:{conferenceName:"PyCon TW",conferenceYear:"2023",conferenceDate:"2023-09-02",showSpeakingPage:b,showAboutStaffPage:a,showSchedulePage:a,showSponsorPage:b,showRegistrationPage:a,showEventOverviewPage:a,showEventsPage:a,showConferencePage:a,showVenuePage:a,showIndexSponsorSection:a,showIndexSecondaryBtn:b,aboutHideItems:["apacCommunity"],eventsHideItems:[],conferenceHideItems:[],registrationHideItems:[],venueHideItems:[]},i18n:{routeParams:{}}},serverRendered:a,routePath:"\u002Fzh-hant\u002Fconference\u002Ftalk\u002F290",config:{gtm:{id:void 0},_app:{basePath:"\u002F2023\u002F",assetsPath:"\u002F2023\u002F_nuxt\u002F",cdnURL:d}}}}(true,false,"",null));