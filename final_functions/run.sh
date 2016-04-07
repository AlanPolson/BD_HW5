#!/bin/bash
MAPPER=$1
REDUCER=$2
INPUT=$3
OUTPUT=$4
LOCAL_OUTPUT=$5
STREAMING_JAR=/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar
hadoop fs -rm -r -skipTrash "${OUTPUT}"
hadoop jar ${STREAMING_JAR} \
    -D mapred.job.name='BDM_Hw5' \
    -D mapred.map.tasks=2 \
    -files "${MAPPER}","${REDUCER}" \
    -mapper "${MAPPER}" \
    -reducer "${REDUCER}" \
    -input "${INPUT}" \
    -output "${OUTPUT}" \
    -numReduceTasks 2

if [ ! -z "${LOCAL_OUTPUT}" ]; then
    rm -f "${LOCAL_OUTPUT}"
    hadoop fs -getmerge "${OUTPUT}/part*" "${LOCAL_OUTPUT}"
fi
