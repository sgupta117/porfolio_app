from django.shortcuts import render

from .models import Projects,Blogs

def index(request):

    myself = '''Hi! I’m Shubham Gupta, working professional software engineer in Gurgaon. 
    I have done my B.E(Hons.) in computer science from BITS PILANI, Pilani (Rajasthan). 
    I try to grab any opportunity I can in developing myself and enhancing my abilities. 
    I am an interesting, fun-loving guy with a good sense of humor.  
    I joke, laugh and humor people and I also get as much as I give. I am a very kind, compassionate, sensitive kind of a guy. 
    I am also a very principled person and stand strong on what is right and wrong. 
    I am also a very straight and honest person.'''

    mrs = Projects()
    mrs.img = 'IPL.jpg'
    mrs.name = 'IPL SCOREE PREDICTOR'
    mrs.desc = 'Makes a prediction of final score of a team based upon the current score/wickets in a match.'
    mrs.liveDemo = 'https://ipl-score-predictor-app.herokuapp.com/'
    mrs.codeLink = 'https://github.com/sgupta117/IPL-Score-Predictor'

    sf = Projects()
    sf.img = 'twitter.png'
    sf.name = 'TWEET ANALYZER'
    sf.desc = "A Cool web app that fetches the last 10 recetn tweets of your favourite personality over tweeter with user sentiment analysis"
    sf.liveDemo = 'https://tweeter-analyzer-app.herokuapp.com/'
    sf.codeLink = 'https://github.com/sgupta117/Tweet-Analyzer'

    hms = Projects()
    hms.img = 'RPS.png'
    hms.name = 'ROCK PAPER SCISSOR GAME'
    hms.desc = "An Rock Paper Scissor AI Game to play with COMPUTER based upon the symbol both makes"
    hms.liveDemo = ''
    hms.codeLink = 'https://github.com/sgupta117/Rock-Paper-Scissor-ML-Game'

    dl = Projects()
    dl.img = 'Stock.png'
    dl.name = 'STOCK MARKET PREDICTION'
    dl.desc = "Predict the stock market prices behaviour and graphs using Long Short Term Memory Algo based upon its past NAV"
    dl.liveDemo = ''
    dl.codeLink = 'https://github.com/sgupta117/Deep-Learning-Projects/tree/master/LSTM/Stock-MArket-Forecasting-master_lstm'

    covid = Projects()
    covid.img = 'flight.jpg'
    covid.name = 'FLIGHT PRICE PREDICTION APP'
    covid.desc = "A simple web app which predicts the fare of Flight tickets."
    covid.liveDemo = 'https://flight-price-prediction-api.herokuapp.com/'
    covid.codeLink = 'https://github.com/sgupta117/Machine-Learning-Projects/tree/master/Flight-Price-Prediction-master'

    ga = Projects()
    ga.img = 'object.png'
    ga.name = 'OBJECT DETECTION USING YOLO'
    ga.desc = "Detection nearby objects using live video streaming and images as well using YOLO Algorithm"
    ga.liveDemo = ''
    ga.codeLink = 'https://github.com/sgupta117/OPEN-CV-Computer-Vision-Projects/tree/master/Object-Detection-Using-YOLO-3-master'

    bcp = Projects()
    bcp.img = 'mask.jpg'
    bcp.name = 'FACE MASK DETECTION'
    bcp.desc = "A Simple app to detect if a person is wearing a mask or not in live video streaming"
    bcp.liveDemo = ''
    bcp.codeLink = 'https://github.com/sgupta117/OPEN-CV-Computer-Vision-Projects/tree/master/Face-Mask-Detector-master'

    ad = Projects()
    ad.img = 'loan.jpg'
    ad.name = "LOAN ELIGIBILITY APP"
    ad.desc = "A web app to check if a person is eligible for taking loan or not based upon its credit score , income and family background."
    ad.liveDemo = 'https://loan-eligibility-check.herokuapp.com/'
    ad.codeLink = 'https://github.com/sgupta117/Machine-Learning-Projects/tree/master/Loan-ELigibility-Checker-Web-App-master'

    ad1 = Projects()
    ad1.img = 'news.jpg'
    ad1.name = "FAKE NEWS CLASSIFIER"
    ad1.desc = "Simple web app to detect if the news is fake or real."
    ad1.liveDemo = 'https://fake-news-classifier-nlp.herokuapp.com/'
    ad1.codeLink = 'https://github.com/sgupta117/Machine-Learning-Projects/tree/master/Fake-News-Classfier-master'

    ad2 = Projects()
    ad2.img = 'fruits.jpg'
    ad2.name = "MULTI FRUIT CLASSIFIER"
    ad2.desc = "This is a simple multicategory prediction model which predicts the kind of fruit based upon the image we provide the model as input."
    ad2.liveDemo = ''
    ad2.codeLink = 'https://github.com/sgupta117/Deep-Learning-Projects/tree/master/MultiFruit-Classification-Using-CNN-master'

    rel = Blogs()
    rel.img = "random_forest.jpeg"
    rel.name = "Random Forest (Easily Explained)"
    rel.desc = "This is a simple multicategory prediction model which predicts the kind of fruit based upon the image we provide the model as input."
    rel.link = "https://medium.com/@gupta020295/random-forest-easily-explained-4b8094feb90"

    dtr = Blogs()
    dtr.img = "imbalanced.jpeg"
    dtr.name = "Handle Imbalanced Dataset"
    dtr.desc = "Blog to make people understand the importance of handling imbalanced dataset while preprocessing the data for any given ML problem statement"
    dtr.link = "https://medium.com/@gupta020295/handle-imbalanced-dataset-5d4b072b8b36"

    gl = Blogs()
    gl.img = "gender.jpeg"
    gl.name = "Gender Detection on real time video streaming"
    gl.desc = "Detect the gender of a person on real live video camera with high accuracy."
    gl.link = "https://medium.com/@gupta020295/gender-detection-on-real-time-video-streaming-89c27b89f51"

    projects = [mrs,sf,hms,dl,covid,ga,bcp,ad,ad1,ad2]
    blogs = [rel,dtr,gl]
    return render(request, 'index.html',{'myself':myself,'projects':projects,'blogs':blogs})
