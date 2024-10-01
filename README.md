# PointPainting
This repository aims to build an open-source PointPainting package which is easy to understand, deploy and run! We refer to the idea in the [original paper](https://arxiv.org/abs/1911.10150) to implement this open-source framework to conduct the sequential 3D object detection. We utilize the Pytorch and mmsegmentation as the image-based segmnentation approach, and the OpenPCDet as the LiDAR detector.

## Update
We propose to support Kitti dataset first and utilize OpenPCDet as the LiDAR detection framework. We are expected to release the code to support Kitti and at least two semantic segmentation methods to do painting by the end of April 2021.  
Update on April 20, 2021: Code released! We currently support Kitti dataset, with DeepLab V3/V3+ and HMA!  
Update on April 25, 2021: You can watch the presentation video at this [link](https://www.youtube.com/watch?v=qtNG_lZuafs&t=11s).

## Table of Contents
- [PointPainting](#pointpainting)
  - [Update](#update)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
    - [Framework Overview](#framework-overview)
  - [Install](#install)
    - [OpenPCDet](#openpcdet)
    - [mmsegmentation](#mmsegmentation)
    - [Hierarchical Multi-Scale Attention for Semantic Segmentation](#hierarchical-multi-scale-attention-for-semantic-segmentation)
  - [How to Use](#how-to-use)
    - [Dataset Preparation](#dataset-preparation)
    - [Painting](#painting)
      - [HMA-based Painting](#hma-based-painting)
    - [LiDAR Detector Training](#lidar-detector-training)
    - [Running Inference](#running-inference)
  - [Results & Discussions](#results--discussions)
    - [Semantic Segmentation](#semantic-segmentation)
    - [Painting](#painting-1)
    - [3D Object Detection](#3d-object-detection)
  - [Authors](#authors)

## Background
The PointPainting means to fuse the semantic segmentation results based on RGB images and add class scores to the raw LiDAR pointcloud to achieve higher accuracy than LiDAR-only approach.

### Framework Overview
The PointPainting architecture consists of three main stages: (1) image based semantics network, (2) fusion (painting), and (3) lidar based detector. In the first step, the images are passed through a semantic segmentation network obtaining pixelwise segmentation scores. In the second stage, the lidar points are projected into the segmentation mask and decorated with the scores obtained in the earlier step. Finally, a lidar based object detector can be used on this decorated (painted) point cloud to obtain 3D detections.
![](figures/framework_overview.png)