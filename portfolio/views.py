from django.shortcuts import render

from .models import Projects,Blogs

def index(request):

    myself = ''' Hi! I’m Shubham Gupta, a working professional software engineer in Gurgaon. 
    I have done my B.E(Hons.) in computer science from BITS PILANI, Pilani (Rajasthan). 
    I try to grab any opportunity I can in developing myself and enhancing my abilities. 
    I am an interesting, fun-loving guy with a good sense of humor.  
    I joke, laugh, and humor people, and I also get as much as I give. I am a very kind, compassionate, sensitive kind of guy. 
    I am also a very principled person and stand strong on what is right and wrong. 
    I am also a very straight and honest person.
    '''

    mrs = Projects()
    mrs.img = 'IPL.jpg'
    mrs.name = 'IPL MATCH SCORE PREDICTOR'
    mrs.desc = 'Machine Learning Project that predicts the IPL match score after 20 overs.'
    mrs.liveDemo = 'https://ipl-score-predictor-app.herokuapp.com/'
    mrs.codeLink = 'https://github.com/sgupta117/IPL-Score-Predictor'

    sf = Projects()
    sf.img = 'twitter.png'
    sf.name = 'TWITTER SENTIMENT ANALYSIS'
    sf.desc = "A Cool web app that fetches the last 10 recent tweets of your favourite personality over tweeter with sentiment analysis of the tweets."
    sf.liveDemo = 'https://tweeter-analyzer-app.herokuapp.com/'
    sf.codeLink = 'https://github.com/sgupta117/Tweet-Analyzer'

    hms = Projects()
    hms.img = 'RPS.jpg'
    hms.name = 'ROCK PAPER SCISSOR GAME'
    hms.desc = "Building a Rock Paper Scissors AI using Tensorflow and OpenCV with Python."
    hms.liveDemo = ''
    hms.codeLink = 'https://github.com/sgupta117/Rock-Paper-Scissor-ML-Game'

    dl = Projects()
    dl.img = 'Stock.png'
    dl.name = 'STOCK PRICE PREDICTION'
    dl.desc = "Bilding a system to predict future stock prices for APPLE company using LSTM Recurrent Neural Network."
    dl.liveDemo = ''
    dl.codeLink = 'https://github.com/sgupta117/Deep-Learning-Projects/tree/master/LSTM/Stock-MArket-Forecasting-master_lstm'

    covid = Projects()
    covid.img = 'flight.jpg'
    covid.name = 'FLIGHT TICKET PRICE PREDICTOR'
    covid.desc = "Building predictive models to predict flight prices in INDIA and to suggest a user whether the prices of a particular flight is expected to rise or fall in future."
    covid.liveDemo = 'https://flight-price-prediction-api.herokuapp.com/'
    covid.codeLink = 'https://github.com/sgupta117/Machine-Learning-Projects/tree/master/Flight-Price-Prediction-master'

    ga = Projects()
    ga.img = 'object.png'
    ga.name = 'OBJECT DETECTION USING YOLO'
    ga.desc = "A python project to detect the real time objects on live video streaming using popular YOLO framework."
    ga.liveDemo = ''
    ga.codeLink = 'https://github.com/sgupta117/OPEN-CV-Computer-Vision-Projects/tree/master/Object-Detection-Using-YOLO-3-master'

    bcp = Projects()
    bcp.img = 'mask.jpg'
    bcp.name = 'FACE MASK DETECTOR'
    bcp.desc = "Building an accurate COVID-19 face mask detector with OpenCV, Keras/TensorFlow, and Deep Learning."
    bcp.liveDemo = ''
    bcp.codeLink = 'https://github.com/sgupta117/OPEN-CV-Computer-Vision-Projects/tree/master/Face-Mask-Detector-master'

    ad = Projects()
    ad.img = 'loan.jpg'
    ad.name = "LOAN ELIGIBILITY APP"
    ad.desc = "A web app to check if a person is eligible for taking loan or not based upon the credit score,income and family background."
    ad.liveDemo = 'https://loan-eligibility-check.herokuapp.com/'
    ad.codeLink = 'https://github.com/sgupta117/Machine-Learning-Projects/tree/master/Loan-ELigibility-Checker-Web-App-master'

    ad1 = Projects()
    ad1.img = 'news.jpg'
    ad1.name = "FAKE NEWS CLASSIFIER"
    ad1.desc = "Building a web app to predict the Fake News using Natural Language Processing."
    ad1.liveDemo = 'https://fake-news-classifier-nlp.herokuapp.com/'
    ad1.codeLink = 'https://github.com/sgupta117/Machine-Learning-Projects/tree/master/Fake-News-Classfier-master'

    ad2 = Projects()
    ad2.img = 'fruits.jpg'
    ad2.name = "MULTI FRUIT CLASSIFIER"
    ad2.desc = "This is a simple multicategory prediction model to classify the fruits using a Keras multi-class image classification model."
    ad2.liveDemo = ''
    ad2.codeLink = 'https://github.com/sgupta117/Deep-Learning-Projects/tree/master/MultiFruit-Classification-Using-CNN-master'

    rel = Blogs()
    rel.img = "random_forest.jpeg"
    rel.name = "Random Forest (Easily Explained)"
    rel.desc = "Simple implementation and understanding of Random Forest algorithm alongside python code."
    rel.link = "https://medium.com/@gupta020295/random-forest-easily-explained-4b8094feb90"

    dtr = Blogs()
    dtr.img = "imbalanced.jpeg"
    dtr.name = "Handle Imbalanced Dataset"
    dtr.desc = "Blog to make people understand the importance of handling imbalanced dataset while preprocessing the data for any given ML problem statement."
    dtr.link = "https://medium.com/@gupta020295/handle-imbalanced-dataset-5d4b072b8b36"

    gl = Blogs()
    gl.img = "gender.jpeg"
    gl.name = "Gender Detection on real time video streaming"
    gl.desc = "Detect the gender of a person on real live video camera with high accuracy."
    gl.link = "https://medium.com/@gupta020295/gender-detection-on-real-time-video-streaming-89c27b89f51"

    projects = [mrs,sf,hms,dl,covid,ga,bcp,ad,ad1,ad2]
    blogs = [rel,dtr,gl]
    return render(request, 'index.html',{'myself':myself,'projects':projects,'blogs':blogs})
