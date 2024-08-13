#!/bin/bash

export AIHUB_ID=$1
export AIHUB_PW=$2

# 
# ./aihubshell -mode d -datasetkey 126

# 전문분야 한영 말뭉치
# ./aihubshell -mode d -datasetkey 111 

# AI 허브 데이터 활용을 위한 기계 번역앱 구축과 번역기 평가 및 신규 말뭉치 구축
# ./aihubshell -mode d -datasetkey 71593

# 다국어 구어체 번역 병렬 말뭉치 데이터
# ./aihubshell -mode d -datasetkey 609

# 산업정보 연계 주요국 특허 영-한 데이터
# ./aihubshell -mode d -datasetkey 563

# 전문분야 영-한·중-한 번역 말뭉치 (식품)
# ./aihubshell -mode d -datasetkey 71262

# 금융 분야 다국어 병렬 말뭉치 데이터
# ./aihubshell -mode d -datasetkey 71782

# 다국어 번역 품질 평가 데이터
# ./aihubshell -mode d -datasetkey 71646

# 국내 법률 대상 다국어 번역 데이터
# ./aihubshell -mode d -datasetkey 71720

# 한-중/한-일 특허 및 기술과학 분야 병렬 말뭉치 데이터
./aihubshell -mode d -datasetkey 71735
