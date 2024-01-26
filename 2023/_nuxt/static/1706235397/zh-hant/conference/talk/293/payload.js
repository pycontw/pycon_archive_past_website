__NUXT_JSONP__("/zh-hant/conference/talk/293", (function(a,b){b.id=293;b.begin_time="2023-09-03T03:35:00Z";b.end_time="2023-09-03T04:05:00Z";b.is_remote=false;b.location="5-r1";b.youtube_id=a;b.title="當AI遇上財經-利用Graph Neural Network分析財經市場 When AI Meets Finance: Using Graph Neural Network to Analyze Financial Market";b.category="FIN";b.language="ZHEN";b.python_level="INTERMEDIATE";b.recording_policy=true;b.abstract="股票與金融市場以其不穩定性及波動性，影響著許多投資人的決策。在世界經濟已被疫情摧殘的當今，只用肉眼預判股價趨勢已經已經略顯不足，伴隨的風險性也隨之提高。隨者計量經濟學的地位提升，經濟統計模型的發展也已經漸漸成熟。然而，統計模型無法紀錄股票\u002F指數之間的複雜關係，更無法根據突發事件調整模型。許多研究已經發現機器學習可以創造出比統計模型更好的預測效果。而且，運用圖神經網路（Graph Neural Network\u002FGNN），機器更可以根據股票\u002F指數之間的關係學習更精確的漲跌關係。\r\n在此演講中，我們會介紹GNN的主要構成元素(nodes 和 edges)，GNN在股票預測的應用和重要性，和探討GNN的種類。接下來，我們會利用 PyTorch Geometric 建立一套結合 GNN 和其他神經網路的模型，並且透過交叉比對其他模型印證 GNN 在財經分析機器學習的重要性。我們也會討論如何利用 python 利用open source抓取股價、利息、匯率等財經資料和交易訊息。";b.detailed_description="### 主要套件\r\n- [**PyTorch Geometric**](https:\u002F\u002Fgithub.com\u002Fpyg-team\u002Fpytorch_geometric): PyTorch 提供的圖神經網路(GNN)套件\r\n- [**yfinance**](https:\u002F\u002Fgithub.com\u002Franaroussi\u002Fyfinance): Yahoo財經，抓取股價的套件\r\n- [**fredapi**](https:\u002F\u002Fgithub.com\u002Fmortada\u002Ffredapi): 美國聯準會資料庫，抓取經濟指數的套件\r\n\r\n### 主要參考論文\r\n- [**Graph neural networks for multivariate time series regression with application to seismic data**](https:\u002F\u002Fdoi.org\u002F10.1007\u002Fs41060-022-00349-6)\r\n    - abstract：利用GNN紀錄地區與地區之間的關係，並更加精確的預測地震波。\r\n- [**Algorithmic Financial Trading with Deep Convolutional Neural Networks: Time Series to Image Conversion Approach**](https:\u002F\u002Fwww.researchgate.net\u002Fpublication\u002F324802031)\r\n    - abstract: 在LSTM上增加一層CNN可幫助機器抓取更多交易信息，使在預測ETF的價格時更佳準確。\r\n- [**HATS: A Hierarchical Graph Attention Network for Stock Movement Prediction**](https:\u002F\u002Farxiv.org\u002Fpdf\u002F1908.07999.pdf)\r\n    - abstract: 利用GAT (GNN 的 attention model) 帶入公司與公司之間的關係圖，進而提升股價的預測準確度。";b.slide_link=a;b.slido_embed_link="https:\u002F\u002Fapp.sli.do\u002Fevent\u002FvxoyxhDW9L6KHG7QhMUws2";b.hackmd_embed_link="https:\u002F\u002Fhackmd.io\u002F@pycontw\u002FrJTvLsXT3";b.speakers=[{thumbnail_url:"https:\u002F\u002Ftw.pycon.org\u002Fprs\u002Fmedia\u002Fcache\u002F34\u002Fce\u002F34ce189363d27d8a6096dbb6f36ca0e0.jpg",name:"William Chang",github_profile_url:a,twitter_profile_url:a,facebook_profile_url:"https:\u002F\u002Fwww.facebook.com\u002Fprofile.php?id=100002638275102",bio:"2022年6月畢業於加拿大多倫多大學。主修經濟學（資料分析專業)，副修政治學和統計學。2022年7月任職於Tagtoo，擔任資料工程師。主要任務為使用使用者行為資料,，建構機器學習模型，提供數位廣告投放策略分析和受眾包預測，並且建立data pipelines進行預測和分析自動化。\r\n\r\nHello, I'm William. I graduated from the University of Toronto in June 2022. I majored in Economics (focus in data analytics) and had two minors in political science and statistics. I started my career in Tagtoo as a data engineer in July 2022. I propose digital marketing strategies and make predictions through machine-learning models by collecting and wrangling our client's data. I also build data pipelines to automate the aforementioned tasks."}];b.event_type="talk";return {data:[{speechData:b}],fetch:{},mutations:[["setSpeechData",b]]}}("",{})));