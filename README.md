# Lane Line Detection System 

## 📌 Project Overview  
This project focuses on developing a **Lane Line Detection System** using **Computer Vision techniques with OpenCV** in Python. The system aims to accurately **detect and track lane lines** from road images and real-time video streams, thereby assisting in **road safety** and forming a core component of **autonomous driving** and **driver assistance systems (ADAS)**.  

## 🎯 Problem Statement  
Develop an automated **Lane Line Detection System** for real-time video and image processing to improve road safety and assist autonomous driving.  
The system should accurately identify and track lane lines on roads under various **environmental conditions** and **road geometries**.

## 🥅 Objectives  
- Develop a computer vision system that can accurately **identify and track lane lines** on roadways.  
- Provide **real-time information** to autonomous vehicles or human drivers.  
- Detect and classify different types of lane lines (solid, dashed).  
- Achieve high accuracy under **various lighting and weather conditions**.  
- Ensure **efficient real-time processing** to support real-world applications.  
- Explore integration with **other advanced driver assistance systems (ADAS)**.  

## 🧠 Concepts & Methods  
The Lane Line Detection pipeline uses:  
- **Grayscale conversion** – simplify images for processing.  
- **Noise reduction (Gaussian Blur)** – remove unnecessary details.  
- **Canny Edge Detection** – extract potential lane boundaries.  
- **Region of Interest (ROI) masking** – focus only on the road area.  
- **Hough Line Transform** – detect straight lane lines.  
- **Color Space Analysis** – distinguish between white and yellow lanes.  
- **Overlaying detected lanes** – project results back on the original video.  

## 🛠️ Tools & Languages  
- **Programming Language**: Python 🐍  
- **Libraries**: OpenCV, NumPy, Matplotlib  
- **IDE**: VS Code  
- **System Used**: HP Pavilion Laptop (16 GB RAM, 1TB storage)  

## ⚙️ Process & Architecture  
**Pipeline Steps**:  
1. Capture video frames / load image.  
2. Convert to grayscale & apply Gaussian blur.  
3. Apply **Canny Edge Detection**.  
4. Define and mask the **Region of Interest (ROI)**.  
5. Use **Hough Line Transform** to detect lane lines.  
6. Post-process and overlay the detected lanes on the original frame.  
7. Display the output in real time.  
