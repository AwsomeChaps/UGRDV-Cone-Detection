#!/usr/bin/python

def ugrdv_challenge_3(left_frame, right_frame):
	mean = []
	for i in range(len(left_frame)):
		mean.append(((left_frame[i][0]+right_frame[i][0])/2, (left_frame[i][1]+right_frame[i][1])/2))
	return mean
