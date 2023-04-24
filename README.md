# Real time Anomaly Detection

Anomaly Detection on AWS using Kinesis Data Firehose and Kinesis Data Analytics App.

This is the supporting repository of the blog post [Real-time Anomaly Detection: How Amazon Kinesis Can Help You Stay Ahead of the Game](https://medium.com/@mrmaheshrajput/real-time-anomaly-detection-how-amazon-kinesis-can-help-you-stay-ahead-of-the-game-229ae8b32e62)

Please read the blog or you can directly check out the `Anomaly_Detection_on_AWS.ipynb` notebook.


## System Design
![System Design](https://cdn-images-1.medium.com/v2/resize:fit:1600/1*jelo3n_abNM8XHLAh5HRlw.jpeg)

## Repository Structure
```
anomaly_detection/
├── src/
│   └── get_pred_from_kinesis.py        # Lambda Function Code
│   └── push_notification_to_sns.py     # Lambda Function Code
│   └── tfrs
├── Anomaly_Detection_on_AWS.ipynb      # Jupyter ipynb
├── LICENSE                             # Apache 2.0 License
├── README.md                           # Repository Readme markdown
```