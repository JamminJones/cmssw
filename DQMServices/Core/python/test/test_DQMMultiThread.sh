#!/bin/bash

clean_files() {
  echo 'Cleaning up files'
  rm -fr *.root
  rm -fr *.sql
  return 0
}

run_step1_edm() {
  echo 'Running first step for MEtoEDM'
  cmsRun dqm_testMultiThread_MEtoEDM_cfg.py &> /dev/null
  if [ $? != 0 ]; then
    exit $?
  fi
}

run_step2_edm() {
  echo 'Running Harvesting for MEtoEDM'
  cmsRun dqm_testMultiThread_HarvestingEDMtoME.py &> /dev/null
  if [ $? != 0 ]; then
    exit $?
  fi
}

check_files() {
filter=$1;shift
 for f in $(ls ${filter}); do
   python check_harvesting.py ${f}
   if [ $? != 0 ]; then
     exit $?
   fi
 done
}

run_step1_dqmio() {
  echo 'Running first step for DQMIO'
  cmsRun dqm_testMultiThread_DQMIO_cfg.py &> /dev/null
  if [ $? != 0 ]; then
    exit $?
  fi
}

run_step2_dqmio() {
  echo 'Running Harvesting for DQMIO'
  cmsRun dqm_testMultiThread_HarvestingDQMIO.py &> /dev/null
  if [ $? != 0 ]; then
    exit $?
  fi
}


clean_files
run_step1_edm
run_step2_edm
check_files "*EDM_Harvesting.root"
run_step1_dqmio
run_step2_dqmio
check_files "*DQMIO_Harvesting.root"

