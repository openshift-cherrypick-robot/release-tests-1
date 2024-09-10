PIPELINES-15
# Verify Addon E2E spec

Pre condition:
  * Validate Operator should be installed

## Disable/Enable community clustertasks: PIPELINES-15-TC01
Tags: e2e, integration, clustertasks, admin, addon, sanity
Component: Pipelines
Level: Integration
Type: Functional
Importance: Critical

Steps:
  * Update addon config with clusterTasks as "true" communityClustertasks as "true" and pipelineTemplates as "true" and expect message ""
  * "community" clustertasks are "present"
  * "tkn,openshift-client" clustertasks are "present"
  * Update addon config with clusterTasks as "true" communityClustertasks as "false" and pipelineTemplates as "true" and expect message ""
  * "community" clustertasks are "not present"
  * "tkn,openshift-client" clustertasks are "present"
  * Update addon config with clusterTasks as "true" communityClustertasks as "true" and pipelineTemplates as "true" and expect message ""
  * "community" clustertasks are "present"
  * "tkn,openshift-client" clustertasks are "present"

## Disable/Enable clustertasks: PIPELINES-15-TC02
Tags: e2e, integration, clustertasks, admin, addon, sanity
Component: Pipelines
Level: Integration
Type: Functional
Importance: Critical

Steps:
  * Update addon config with clusterTasks as "true" communityClustertasks as "true" and pipelineTemplates as "true" and expect message ""
  * "community" clustertasks are "present"
  * "tkn,openshift-client" clustertasks are "present"
  * Assert pipelines are "present" in "openshift" namespace
  * Update addon config with clusterTasks as "false" communityClustertasks as "false" and pipelineTemplates as "false" and expect message ""
  * "community" clustertasks are "not present"
  * "tkn,openshift-client" clustertasks are "not present"
  * Assert pipelines are "not present" in "openshift" namespace
  * Update addon config with clusterTasks as "true" communityClustertasks as "true" and pipelineTemplates as "true" and expect message ""
  * "community" clustertasks are "present"
  * "tkn,openshift-client" clustertasks are "present"
  * Assert pipelines are "present" in "openshift" namespace

## Disable/Enable pipeline templates: PIPELINES-15-TC03
Tags: e2e, integration, clustertasks, admin, addon, sanity
Component: Pipelines
Level: Integration
Type: Functional
Importance: Critical

Steps:
  * Update addon config with clusterTasks as "true" communityClustertasks as "true" and pipelineTemplates as "true" and expect message ""
  * Assert pipelines are "present" in "openshift" namespace
  * Update addon config with clusterTasks as "true" communityClustertasks as "true" and pipelineTemplates as "false" and expect message ""
  * Assert pipelines are "not present" in "openshift" namespace
  * Update addon config with clusterTasks as "true" communityClustertasks as "true" and pipelineTemplates as "true" and expect message ""
  * Assert pipelines are "present" in "openshift" namespace

## Enable community cluster tasks when clustertask is disabled: PIPELINES-15-TC04
Tags: e2e, integration, negative, admin, addon
Component: Pipelines
Level: Integration
Type: Functional
Importance: Critical
Pos/Neg: Negative

Steps:
  * Update addon config with clusterTasks as "false" communityClustertasks as "true" and pipelineTemplates as "false" and expect message "validation failed: communityClusterTasks cannot be true if clusterTask is false"

## Enable pipeline templates when clustertask is disabled: PIPELINES-15-TC05
Tags: e2e, integration, negative, admin, addon
Component: Pipelines
Level: Integration
Type: Functional
Importance: Critical
Pos/Neg: Negative

Steps:
  * Update addon config with clusterTasks as "false" communityClustertasks as "false" and pipelineTemplates as "true" and expect message "validation failed: pipelineTemplates cannot be true if clusterTask is false"

## Disable/Enable resolverTasks: PIPELINES-15-TC06
Tags: e2e, integration, resolverTasks, admin, addon, sanity
Component: Pipelines
Level: Integration
Type: Functional
Importance: Critical

Steps:
  * Update addon config with resolverTasks as "false" and expect message ""
  * Tasks "s2i-java" are "not present" in namespace "openshift-pipelines"
  * Update addon config with resolverTasks as "true" and expect message ""
  * Tasks "s2i-java" are "present" in namespace "openshift-pipelines"

## Disable/Enable resolverTasks with additional Tasks: PIPELINES-15-TC07
Tags: e2e, integration, resolverTasks, admin, addon
Component: Pipelines
Level: Integration
Type: Functional
Importance: Critical

Steps:
  * Update addon config with resolverTasks as "true" and expect message ""
  * Tasks "s2i-java" are "present" in namespace "openshift-pipelines"
  * Apply in namespace "openshift-pipelines"
      |S.NO|resource_dir                                         |
      |----|-----------------------------------------------------|
      |1   |testdata/ecosystem/tasks/hello.yaml                  |
  * Tasks "hello" are "present" in namespace "openshift-pipelines"
  * Update addon config with resolverTasks as "false" and expect message ""
  * Tasks "s2i-java" are "not present" in namespace "openshift-pipelines"
  * Tasks "hello" are "present" in namespace "openshift-pipelines"
  * Update addon config with resolverTasks as "true" and expect message ""
  * Tasks "s2i-java" are "present" in namespace "openshift-pipelines"
  * Tasks "hello" are "present" in namespace "openshift-pipelines"

