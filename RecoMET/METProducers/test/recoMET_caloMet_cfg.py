import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("TEST")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

##____________________________________________________________________________||
process.load("RecoMET.Configuration.CaloTowersOptForMET_cff")
process.load("RecoMET.Configuration.RecoMET_cff")
process.load("RecoJets.Configuration.CaloTowersRec_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("RecoLocalCalo.Configuration.RecoLocalCalo_cff")

##____________________________________________________________________________||
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

##____________________________________________________________________________||
from RecoMET.METProducers.testInputFiles_cff import recoMETtestInputFiles

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(recoMETtestInputFiles)
    )

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('recoMET_caloMet.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_*_*_METP'
        )
    )

##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

##____________________________________________________________________________||
process.p = cms.Path(
    process.calotoweroptmaker *
    process.calotoweroptmakerWithHO *
    process.towerMakerWithHO *
    process.met *
    process.metNoHF *
    process.metHO *
    process.metNoHFHO *
    process.metOpt *
    process.metOptNoHF *
    process.metOptHO *
    process.metOptNoHFHO *
    process.corMetGlobalMuons
    )

process.e1 = cms.EndPath(
    process.out
    )

##____________________________________________________________________________||
