# pylint: disable=too-many-lines
cached = [
    "aws-apigatewayv2-integration.json",
    "aws-apigatewayv2-apimapping.json",
    "aws-sso-assignment.json",
    "aws-glue-partition.json",
    "aws-ec2-transitgatewayroutetablepropagation.json",
    "aws-ssm-resourcepolicy.json",
    "aws-apigateway-basepathmapping.json",
    "aws-wafregional-geomatchset.json",
    "aws-guardduty-filter.json",
    "aws-ecs-service.json",
    "aws-servicecatalog-portfolioprincipalassociation.json",
    "aws-ram-resourceshare.json",
    "aws-memorydb-cluster.json",
    "aws-dynamodb-table.json",
    "aws-amazonmq-configurationassociation.json",
    "aws-wafregional-ipset.json",
    "aws-redshiftserverless-namespace.json",
    "aws-ec2-securitygroupegress.json",
    "aws-ec2-localgatewayroutetablevpcassociation.json",
    "aws-config-organizationconfigrule.json",
    "aws-config-configurationrecorder.json",
    "aws-ec2-networkperformancemetricsubscription.json",
    "aws-medialive-channel.json",
    "aws-greengrass-devicedefinition.json",
    "aws-cloudfront-continuousdeploymentpolicy.json",
    "aws-quicksight-analysis.json",
    "aws-ecr-replicationconfiguration.json",
    "aws-s3outposts-accesspoint.json",
    "aws-mediapackage-originendpoint.json",
    "aws-ec2-ipampoolcidr.json",
    "aws-iot-topicruledestination.json",
    "aws-amplify-branch.json",
    "aws-redshift-clustersubnetgroup.json",
    "aws-rds-dbinstance.json",
    "aws-ec2-vpcdhcpoptionsassociation.json",
    "aws-lightsail-bucket.json",
    "aws-apigateway-model.json",
    "aws-apigatewayv2-integrationresponse.json",
    "aws-iotevents-input.json",
    "aws-ec2-networkacl.json",
    "aws-lambda-eventsourcemapping.json",
    "aws-budgets-budgetsaction.json",
    "aws-logs-resourcepolicy.json",
    "aws-lex-botversion.json",
    "aws-servicecatalog-launchnotificationconstraint.json",
    "aws-quicksight-datasource.json",
    "aws-iot-cacertificate.json",
    "aws-ec2-networkaclentry.json",
    "aws-ec2-networkinsightsaccessscopeanalysis.json",
    "aws-transfer-certificate.json",
    "aws-connect-instance.json",
    "aws-apigateway-documentationpart.json",
    "aws-cloudwatch-compositealarm.json",
    "aws-route53resolver-firewalldomainlist.json",
    "aws-redshift-endpointaccess.json",
    "aws-appconfig-application.json",
    "aws-ivschat-loggingconfiguration.json",
    "aws-opsworks-stack.json",
    "aws-lambda-url.json",
    "aws-gamelift-fleet.json",
    "aws-datasync-locationfsxwindows.json",
    "aws-gamelift-build.json",
    "aws-apigateway-requestvalidator.json",
    "aws-autoscaling-warmpool.json",
    "aws-applicationautoscaling-scalabletarget.json",
    "aws-apigatewayv2-model.json",
    "aws-config-storedquery.json",
    "aws-acmpca-permission.json",
    "aws-neptune-dbsubnetgroup.json",
    "aws-cassandra-keyspace.json",
    "aws-transfer-server.json",
    "aws-apigateway-domainname.json",
    "aws-ecs-primarytaskset.json",
    "aws-fms-resourceset.json",
    "aws-cognito-userpooldomain.json",
    "aws-autoscaling-autoscalinggroup.json",
    "aws-wafv2-regexpatternset.json",
    "aws-eks-fargateprofile.json",
    "aws-route53-dnssec.json",
    "aws-redshift-endpointauthorization.json",
    "aws-ec2-transitgatewayroutetable.json",
    "aws-controltower-enabledcontrol.json",
    "aws-lightsail-container.json",
    "aws-macie-customdataidentifier.json",
    "aws-cognito-identitypoolroleattachment.json",
    "aws-route53-recordset.json",
    "aws-mediastore-container.json",
    "aws-amplifyuibuilder-form.json",
    "aws-ivs-streamkey.json",
    "aws-elasticache-securitygroup.json",
    "aws-backup-framework.json",
    "aws-appflow-connectorprofile.json",
    "aws-pinpoint-emailchannel.json",
    "aws-rekognition-collection.json",
    "aws-opsworks-layer.json",
    "aws-cloudtrail-eventdatastore.json",
    "aws-kinesisfirehose-deliverystream.json",
    "aws-ec2-networkinsightsaccessscope.json",
    "aws-cognito-userpoolusertogroupattachment.json",
    "aws-mediaconvert-queue.json",
    "aws-sagemaker-coderepository.json",
    "aws-imagebuilder-component.json",
    "aws-ses-configurationseteventdestination.json",
    "aws-mediapackage-packagingconfiguration.json",
    "aws-mediaconnect-flowentitlement.json",
    "aws-glue-connection.json",
    "aws-appmesh-route.json",
    "aws-iam-group.json",
    "aws-macie-findingsfilter.json",
    "aws-organizations-resourcepolicy.json",
    "aws-wafregional-webaclassociation.json",
    "aws-ec2-transitgatewaymulticastgroupsource.json",
    "aws-pinpoint-applicationsettings.json",
    "aws-lex-bot.json",
    "aws-transfer-profile.json",
    "aws-databrew-recipe.json",
    "aws-gamelift-alias.json",
    "aws-appsync-domainname.json",
    "aws-pinpoint-pushtemplate.json",
    "aws-apigateway-usageplankey.json",
    "aws-fms-policy.json",
    "aws-greengrass-functiondefinition.json",
    "aws-lightsail-staticip.json",
    "aws-cloudfront-realtimelogconfig.json",
    "aws-sagemaker-pipeline.json",
    "aws-cloudtrail-channel.json",
    "aws-docdb-dbinstance.json",
    "aws-lakeformation-datacellsfilter.json",
    "aws-datasync-locationhdfs.json",
    "aws-iotsitewise-portal.json",
    "aws-events-archive.json",
    "aws-msk-cluster.json",
    "aws-codepipeline-pipeline.json",
    "aws-opsworks-instance.json",
    "aws-config-configurationaggregator.json",
    "aws-imagebuilder-imagepipeline.json",
    "aws-elasticloadbalancingv2-listenercertificate.json",
    "aws-cloudformation-moduleversion.json",
    "aws-cloud9-environmentec2.json",
    "aws-route53resolver-resolverruleassociation.json",
    "aws-fsx-storagevirtualmachine.json",
    "aws-greengrass-connectordefinitionversion.json",
    "aws-synthetics-canary.json",
    "aws-kinesisanalyticsv2-applicationcloudwatchloggingoption.json",
    "aws-sns-subscription.json",
    "aws-appmesh-mesh.json",
    "aws-ec2-natgateway.json",
    "aws-greengrass-connectordefinition.json",
    "aws-internetmonitor-monitor.json",
    "aws-transfer-workflow.json",
    "aws-qldb-ledger.json",
    "aws-appconfig-deploymentstrategy.json",
    "aws-glue-devendpoint.json",
    "aws-sagemaker-modelpackage.json",
    "aws-customerprofiles-integration.json",
    "aws-workspaces-connectionalias.json",
    "aws-wafregional-sizeconstraintset.json",
    "aws-eventschemas-discoverer.json",
    "aws-elasticache-usergroup.json",
    "aws-imagebuilder-imagerecipe.json",
    "aws-apigateway-restapi.json",
    "aws-opsworks-elasticloadbalancerattachment.json",
    "aws-mediaconvert-jobtemplate.json",
    "aws-appmesh-virtualservice.json",
    "aws-s3objectlambda-accesspointpolicy.json",
    "aws-networkmanager-transitgatewayregistration.json",
    "aws-amplify-app.json",
    "aws-inspectorv2-filter.json",
    "aws-elasticache-replicationgroup.json",
    "aws-cassandra-table.json",
    "aws-cognito-userpoolresourceserver.json",
    "aws-rds-globalcluster.json",
    "aws-cloudformation-moduledefaultversion.json",
    "aws-ce-costcategory.json",
    "aws-sso-permissionset.json",
    "aws-glue-job.json",
    "aws-servicecatalog-cloudformationprovisionedproduct.json",
    "aws-resourceexplorer2-index.json",
    "aws-glue-table.json",
    "aws-wafregional-webacl.json",
    "aws-logs-metricfilter.json",
    "aws-lambda-function.json",
    "aws-sns-topic.json",
    "aws-backup-backupselection.json",
    "aws-datasync-locationfsxlustre.json",
    "aws-sagemaker-app.json",
    "aws-ec2-vpcgatewayattachment.json",
    "aws-cloudtrail-trail.json",
    "aws-ec2-vpnconnectionroute.json",
    "aws-kafkaconnect-connector.json",
    "aws-gamelift-gameservergroup.json",
    "aws-appstream-stack.json",
    "aws-ec2-internetgateway.json",
    "aws-ec2-gatewayroutetableassociation.json",
    "aws-wafv2-ipset.json",
    "aws-greengrass-subscriptiondefinition.json",
    "aws-greengrass-group.json",
    "aws-ssm-document.json",
    "aws-iam-role.json",
    "aws-events-apidestination.json",
    "aws-dms-endpoint.json",
    "aws-iotsitewise-project.json",
    "aws-cloudfront-cloudfrontoriginaccessidentity.json",
    "aws-codestarnotifications-notificationrule.json",
    "aws-sagemaker-endpointconfig.json",
    "aws-appmesh-gatewayroute.json",
    "aws-apigateway-apikey.json",
    "aws-gamelift-location.json",
    "aws-autoscaling-launchconfiguration.json",
    "aws-apigateway-clientcertificate.json",
    "aws-kinesisanalyticsv2-application.json",
    "aws-lambda-alias.json",
    "aws-waf-ipset.json",
    "aws-ec2-transitgatewaymulticastdomainassociation.json",
    "aws-s3outposts-endpoint.json",
    "aws-waf-sizeconstraintset.json",
    "aws-ec2-transitgatewayroutetableassociation.json",
    "aws-appconfig-environment.json",
    "aws-imagebuilder-image.json",
    "aws-elasticache-securitygroupingress.json",
    "aws-wafregional-xssmatchset.json",
    "aws-rds-dbproxytargetgroup.json",
    "aws-cloudwatch-dashboard.json",
    "aws-cloudwatch-alarm.json",
    "aws-ec2-carriergateway.json",
    "aws-guardduty-member.json",
    "aws-groundstation-missionprofile.json",
    "aws-cloudformation-customresource.json",
    "aws-kinesisanalytics-applicationoutput.json",
    "aws-wafv2-rulegroup.json",
    "aws-sagemaker-modelpackagegroup.json",
    "aws-ses-configurationset.json",
    "aws-elasticache-parametergroup.json",
    "aws-networkfirewall-loggingconfiguration.json",
    "aws-glue-classifier.json",
    "aws-codedeploy-deploymentgroup.json",
    "aws-amplifyuibuilder-component.json",
    "aws-sagemaker-inferenceexperiment.json",
    "aws-cloudformation-stackset.json",
    "aws-ec2-route.json",
    "aws-fis-experimenttemplate.json",
    "aws-codecommit-repository.json",
    "aws-cloudformation-hookversion.json",
    "aws-rolesanywhere-profile.json",
    "aws-xray-resourcepolicy.json",
    "aws-iot-resourcespecificlogging.json",
    "aws-servicecatalog-launchtemplateconstraint.json",
    "aws-devopsguru-resourcecollection.json",
    "aws-wafv2-loggingconfiguration.json",
    "aws-dynamodb-globaltable.json",
    "alexa-ask-skill.json",
    "aws-backup-backupplan.json",
    "aws-pinpoint-eventstream.json",
    "aws-imagebuilder-distributionconfiguration.json",
    "aws-lakeformation-permissions.json",
    "aws-resourceexplorer2-view.json",
    "aws-glue-datacatalogencryptionsettings.json",
    "aws-cloudfront-publickey.json",
    "aws-lex-botalias.json",
    "aws-identitystore-group.json",
    "aws-datasync-task.json",
    "aws-ecs-taskdefinition.json",
    "aws-sagemaker-model.json",
    "aws-memorydb-parametergroup.json",
    "aws-appstream-appblock.json",
    "aws-ses-vdmattributes.json",
    "aws-identitystore-groupmembership.json",
    "aws-appsync-functionconfiguration.json",
    "aws-ec2-spotfleet.json",
    "aws-glue-schemaversion.json",
    "aws-sagemaker-space.json",
    "aws-iot-policyprincipalattachment.json",
    "aws-fms-notificationchannel.json",
    "aws-msk-batchscramsecret.json",
    "aws-dms-certificate.json",
    "aws-s3-bucket.json",
    "aws-guardduty-ipset.json",
    "aws-servicediscovery-httpnamespace.json",
    "aws-emr-securityconfiguration.json",
    "aws-cloudwatch-insightrule.json",
    "aws-apigateway-usageplan.json",
    "aws-appintegrations-eventintegration.json",
    "aws-batch-schedulingpolicy.json",
    "aws-iot-authorizer.json",
    "aws-apigatewayv2-vpclink.json",
    "aws-iot-jobtemplate.json",
    "aws-servicecatalog-portfolioproductassociation.json",
    "aws-databrew-project.json",
    "aws-athena-workgroup.json",
    "aws-sagemaker-imageversion.json",
    "aws-apigatewayv2-api.json",
    "aws-detective-graph.json",
    "aws-servicecatalog-portfolioshare.json",
    "aws-connect-integrationassociation.json",
    "aws-networkmanager-customergatewayassociation.json",
    "aws-iam-servercertificate.json",
    "aws-codestarconnections-connection.json",
    "aws-iot-securityprofile.json",
    "aws-events-eventbus.json",
    "aws-autoscalingplans-scalingplan.json",
    "aws-ssm-maintenancewindowtarget.json",
    "aws-apigateway-authorizer.json",
    "aws-appstream-imagebuilder.json",
    "aws-lightsail-disk.json",
    "aws-iam-policy.json",
    "aws-databrew-schedule.json",
    "aws-connect-approvedorigin.json",
    "aws-ses-contactlist.json",
    "aws-connect-securitykey.json",
    "aws-cloudformation-publisher.json",
    "aws-rds-dbsecuritygroupingress.json",
    "aws-iotevents-detectormodel.json",
    "aws-appstream-stackfleetassociation.json",
    "aws-ssmcontacts-contact.json",
    "aws-ec2-transitgatewaymulticastgroupmember.json",
    "aws-ec2-volumeattachment.json",
    "aws-glue-securityconfiguration.json",
    "aws-databrew-ruleset.json",
    "aws-gamelift-matchmakingconfiguration.json",
    "aws-applicationinsights-application.json",
    "aws-ecs-clustercapacityproviderassociations.json",
    "aws-appconfig-configurationprofile.json",
    "aws-managedblockchain-node.json",
    "aws-route53resolver-firewallrulegroup.json",
    "aws-msk-configuration.json",
    "aws-ec2-transitgateway.json",
    "aws-cognito-userpoolgroup.json",
    "aws-ec2-vpcendpointservicepermissions.json",
    "aws-ssm-maintenancewindowtask.json",
    "aws-ec2-transitgatewaymulticastdomain.json",
    "aws-eks-cluster.json",
    "aws-codebuild-project.json",
    "aws-efs-filesystem.json",
    "aws-pinpoint-apnsvoipsandboxchannel.json",
    "aws-config-organizationconformancepack.json",
    "aws-logs-querydefinition.json",
    "aws-iam-instanceprofile.json",
    "aws-appstream-application.json",
    "aws-datasync-locationnfs.json",
    "aws-amplify-domain.json",
    "aws-kinesisanalyticsv2-applicationoutput.json",
    "aws-ivs-recordingconfiguration.json",
    "aws-medialive-inputsecuritygroup.json",
    "aws-sagemaker-domain.json",
    "aws-greengrass-coredefinitionversion.json",
    "aws-certificatemanager-certificate.json",
    "aws-glue-schemaversionmetadata.json",
    "aws-sdb-domain.json",
    "aws-ec2-subnetroutetableassociation.json",
    "aws-servicecatalog-serviceactionassociation.json",
    "aws-cognito-userpooluicustomizationattachment.json",
    "aws-sagemaker-notebookinstancelifecycleconfig.json",
    "aws-imagebuilder-containerrecipe.json",
    "aws-connect-rule.json",
    "aws-efs-accesspoint.json",
    "aws-redshift-clustersecuritygroupingress.json",
    "aws-servicecatalogappregistry-attributegroupassociation.json",
    "aws-elasticloadbalancingv2-loadbalancer.json",
    "aws-opensearchservice-domain.json",
    "aws-servicediscovery-instance.json",
    "aws-elasticsearch-domain.json",
    "aws-personalize-solution.json",
    "aws-kinesisanalytics-application.json",
    "aws-apigatewayv2-deployment.json",
    "aws-servicecatalog-stacksetconstraint.json",
    "aws-ivs-channel.json",
    "aws-memorydb-user.json",
    "aws-ec2-networkinterfacepermission.json",
    "aws-servicecatalog-tagoption.json",
    "aws-servicediscovery-privatednsnamespace.json",
    "aws-servicecatalog-launchroleconstraint.json",
    "aws-iot-rolealias.json",
    "aws-sagemaker-modelbiasjobdefinition.json",
    "aws-secretsmanager-resourcepolicy.json",
    "aws-cloudformation-hookdefaultversion.json",
    "aws-config-configrule.json",
    "aws-ec2-networkinsightsanalysis.json",
    "aws-ec2-clientvpnroute.json",
    "aws-ecs-taskset.json",
    "aws-appsync-apikey.json",
    "aws-cloudformation-typeactivation.json",
    "aws-groundstation-dataflowendpointgroup.json",
    "aws-acmpca-certificateauthorityactivation.json",
    "aws-guardduty-threatintelset.json",
    "aws-wafregional-ratebasedrule.json",
    "aws-kinesisvideo-signalingchannel.json",
    "aws-redshiftserverless-workgroup.json",
    "aws-macie-allowlist.json",
    "aws-ec2-vpc.json",
    "aws-iotsitewise-asset.json",
    "aws-dms-replicationsubnetgroup.json",
    "aws-s3outposts-bucket.json",
    "aws-route53-recordsetgroup.json",
    "aws-appstream-applicationentitlementassociation.json",
    "aws-kinesisanalytics-applicationreferencedatasource.json",
    "aws-ec2-localgatewayroute.json",
    "aws-cloudformation-publictypeversion.json",
    "aws-iotsitewise-accesspolicy.json",
    "aws-opsworks-app.json",
    "aws-kinesis-stream.json",
    "aws-greengrass-coredefinition.json",
    "aws-backup-reportplan.json",
    "aws-batch-jobdefinition.json",
    "aws-iam-samlprovider.json",
    "aws-lightsail-database.json",
    "aws-appflow-connector.json",
    "aws-lightsail-loadbalancer.json",
    "aws-cloudfront-keygroup.json",
    "aws-ec2-networkinterfaceattachment.json",
    "aws-ec2-transitgatewayattachment.json",
    "aws-cognito-userpooluser.json",
    "aws-connect-contactflowmodule.json",
    "aws-codedeploy-deploymentconfig.json",
    "aws-iotsitewise-assetmodel.json",
    "aws-networkmanager-globalnetwork.json",
    "aws-connect-tasktemplate.json",
    "aws-pinpoint-apnssandboxchannel.json",
    "aws-servicecatalogappregistry-application.json",
    "aws-networkmanager-site.json",
    "aws-glue-database.json",
    "aws-neptune-dbcluster.json",
    "aws-backup-backupvault.json",
    "aws-ec2-customergateway.json",
    "aws-waf-bytematchset.json",
    "aws-amplifyuibuilder-theme.json",
    "aws-emrserverless-application.json",
    "aws-ec2-host.json",
    "aws-forecast-datasetgroup.json",
    "aws-appstream-user.json",
    "aws-lambda-codesigningconfig.json",
    "aws-comprehend-flywheel.json",
    "aws-systemsmanagersap-application.json",
    "aws-dms-replicationtask.json",
    "aws-ec2-routetable.json",
    "aws-rds-dbproxyendpoint.json",
    "aws-datasync-locationsmb.json",
    "aws-resiliencehub-app.json",
    "aws-rolesanywhere-crl.json",
    "aws-redshift-clusterparametergroup.json",
    "aws-organizations-policy.json",
    "aws-glue-trigger.json",
    "aws-globalaccelerator-listener.json",
    "aws-signer-signingprofile.json",
    "aws-ec2-vpcpeeringconnection.json",
    "aws-sns-topicpolicy.json",
    "aws-mwaa-environment.json",
    "aws-elasticache-globalreplicationgroup.json",
    "aws-networkfirewall-rulegroup.json",
    "aws-route53resolver-resolverdnssecconfig.json",
    "aws-servicecatalog-acceptedportfolioshare.json",
    "aws-route53resolver-firewallrulegroupassociation.json",
    "aws-route53resolver-resolverqueryloggingconfig.json",
    "aws-ec2-subnet.json",
    "aws-cloudtrail-resourcepolicy.json",
    "aws-s3objectlambda-accesspoint.json",
    "aws-lightsail-instance.json",
    "aws-waf-rule.json",
    "aws-elasticbeanstalk-configurationtemplate.json",
    "aws-sqs-queuepolicy.json",
    "aws-appsync-domainnameapiassociation.json",
    "aws-appsync-apicache.json",
    "aws-apigateway-account.json",
    "aws-wafv2-webacl.json",
    "aws-globalaccelerator-endpointgroup.json",
    "aws-ec2-transitgatewayconnect.json",
    "aws-emrcontainers-virtualcluster.json",
    "aws-ec2-securitygroup.json",
    "aws-quicksight-theme.json",
    "aws-ec2-capacityreservationfleet.json",
    "aws-opsworks-volume.json",
    "aws-ses-emailidentity.json",
    "aws-iam-usertogroupaddition.json",
    "aws-events-rule.json",
    "aws-gamelift-gamesessionqueue.json",
    "aws-databrew-dataset.json",
    "aws-ec2-vpngatewayroutepropagation.json",
    "aws-glue-crawler.json",
    "aws-cloudfront-function.json",
    "aws-apigateway-method.json",
    "aws-wafregional-regexpatternset.json",
    "aws-ssm-patchbaseline.json",
    "aws-servicediscovery-service.json",
    "aws-customerprofiles-objecttype.json",
    "aws-cloudfront-monitoringsubscription.json",
    "aws-iotevents-alarmmodel.json",
    "aws-efs-mounttarget.json",
    "aws-quicksight-dataset.json",
    "aws-ec2-vpnconnection.json",
    "aws-waf-webacl.json",
    "aws-servicediscovery-publicdnsnamespace.json",
    "aws-iam-user.json",
    "aws-emr-instancegroupconfig.json",
    "aws-mediaconnect-flow.json",
    "aws-stepfunctions-activity.json",
    "aws-synthetics-group.json",
    "aws-forecast-dataset.json",
    "aws-sagemaker-project.json",
    "aws-ec2-localgatewayroutetablevirtualinterfacegroupassociation.json",
    "aws-s3-bucketpolicy.json",
    "aws-appsync-graphqlschema.json",
    "aws-iot-custommetric.json",
    "aws-redshift-cluster.json",
    "aws-codebuild-sourcecredential.json",
    "aws-emr-instancefleetconfig.json",
    "aws-emr-cluster.json",
    "aws-codepipeline-webhook.json",
    "aws-apigatewayv2-domainname.json",
    "aws-rds-dbcluster.json",
    "aws-servicecatalog-resourceupdateconstraint.json",
    "aws-transfer-agreement.json",
    "aws-lightsail-certificate.json",
    "aws-chatbot-slackchannelconfiguration.json",
    "aws-cloudfront-distribution.json",
    "aws-elasticache-subnetgroup.json",
    "aws-xray-group.json",
    "aws-lookoutvision-project.json",
    "aws-oam-link.json",
    "aws-iot-domainconfiguration.json",
    "aws-sagemaker-endpoint.json",
    "aws-networkfirewall-firewall.json",
    "aws-eventschemas-schema.json",
    "aws-m2-application.json",
    "aws-lookoutequipment-inferencescheduler.json",
    "aws-ses-template.json",
    "aws-redshift-clustersecuritygroup.json",
    "aws-route53-cidrcollection.json",
    "aws-ecr-pullthroughcacherule.json",
    "aws-glue-mltransform.json",
    "aws-appconfig-hostedconfigurationversion.json",
    "aws-datasync-locationefs.json",
    "aws-ec2-localgatewayroutetable.json",
    "aws-apigateway-resource.json",
    "aws-sagemaker-appimageconfig.json",
    "aws-macie-session.json",
    "aws-elasticloadbalancingv2-targetgroup.json",
    "aws-applicationautoscaling-scalingpolicy.json",
    "aws-pipes-pipe.json",
    "aws-iotsitewise-gateway.json",
    "aws-emr-studiosessionmapping.json",
    "aws-ivs-playbackkeypair.json",
    "aws-cloudformation-macro.json",
    "aws-sagemaker-workteam.json",
    "aws-ssmincidents-responseplan.json",
    "aws-lambda-layerversionpermission.json",
    "aws-secretsmanager-secret.json",
    "aws-elasticache-user.json",
    "aws-sagemaker-image.json",
    "aws-logs-subscriptionfilter.json",
    "aws-codedeploy-application.json",
    "aws-dms-eventsubscription.json",
    "aws-ssmincidents-replicationset.json",
    "aws-lakeformation-principalpermissions.json",
    "aws-datasync-locations3.json",
    "aws-mediaconvert-preset.json",
    "aws-autoscaling-lifecyclehook.json",
    "aws-fsx-datarepositoryassociation.json",
    "aws-ec2-networkinterface.json",
    "aws-sagemaker-featuregroup.json",
    "aws-appsync-resolver.json",
    "aws-rolesanywhere-trustanchor.json",
    "aws-route53resolver-resolverqueryloggingconfigassociation.json",
    "aws-kinesisanalyticsv2-applicationreferencedatasource.json",
    "aws-lambda-eventinvokeconfig.json",
    "aws-mediaconnect-flowoutput.json",
    "aws-lambda-layerversion.json",
    "aws-kinesisvideo-stream.json",
    "aws-rds-optiongroup.json",
    "aws-opsworks-userprofile.json",
    "aws-glue-schema.json",
    "aws-docdb-dbsubnetgroup.json",
    "aws-servicecatalog-portfolio.json",
    "aws-customerprofiles-domain.json",
    "aws-iot-policy.json",
    "aws-ec2-transitgatewayroute.json",
    "aws-ssm-maintenancewindow.json",
    "aws-lakeformation-tagassociation.json",
    "aws-rekognition-project.json",
    "aws-ec2-ipamresourcediscovery.json",
    "aws-greengrassv2-componentversion.json",
    "aws-m2-environment.json",
    "aws-pinpoint-campaign.json",
    "aws-imagebuilder-infrastructureconfiguration.json",
    "aws-iot-logging.json",
    "aws-medialive-input.json",
    "aws-cloudformation-waitcondition.json",
    "aws-route53resolver-resolverendpoint.json",
    "aws-iot-scheduledaudit.json",
    "aws-connect-contactflow.json",
    "aws-networkmanager-link.json",
    "aws-qldb-stream.json",
    "aws-sagemaker-notebookinstance.json",
    "aws-iotsitewise-dashboard.json",
    "aws-pinpoint-apnsvoipchannel.json",
    "aws-sso-instanceaccesscontrolattributeconfiguration.json",
    "aws-wafregional-bytematchset.json",
    "aws-cloudwatch-anomalydetector.json",
    "aws-ec2-subnetnetworkaclassociation.json",
    "aws-servicecatalog-serviceaction.json",
    "aws-appstream-entitlement.json",
    "aws-cloudfront-originaccesscontrol.json",
    "aws-iot-mitigationaction.json",
    "aws-cognito-userpool.json",
    "aws-secretsmanager-rotationschedule.json",
    "aws-lambda-permission.json",
    "aws-networkfirewall-firewallpolicy.json",
    "aws-eks-identityproviderconfig.json",
    "aws-ec2-ipamresourcediscoveryassociation.json",
    "aws-servicecatalogappregistry-attributegroup.json",
    "aws-lightsail-loadbalancertlscertificate.json",
    "aws-ec2-clientvpntargetnetworkassociation.json",
    "aws-appsync-graphqlapi.json",
    "aws-gamelift-matchmakingruleset.json",
    "aws-ec2-egressonlyinternetgateway.json",
    "aws-config-conformancepack.json",
    "aws-ec2-vpccidrblock.json",
    "aws-gamelift-script.json",
    "aws-iam-virtualmfadevice.json",
    "aws-ec2-networkinsightspath.json",
    "aws-acmpca-certificateauthority.json",
    "aws-athena-preparedstatement.json",
    "aws-autoscaling-scheduledaction.json",
    "aws-apigatewayv2-route.json",
    "aws-lakeformation-resource.json",
    "aws-detective-memberinvitation.json",
    "aws-ec2-ipamscope.json",
    "aws-sagemaker-dataqualityjobdefinition.json",
    "aws-cloudfront-streamingdistribution.json",
    "aws-personalize-datasetgroup.json",
    "aws-rds-eventsubscription.json",
    "aws-config-aggregationauthorization.json",
    "aws-datasync-agent.json",
    "aws-cognito-userpoolidentityprovider.json",
    "aws-appstream-stackuserassociation.json",
    "aws-resiliencehub-resiliencypolicy.json",
    "aws-iot-dimension.json",
    "aws-ecs-cluster.json",
    "aws-s3-multiregionaccesspointpolicy.json",
    "aws-ec2-trafficmirrorfilterrule.json",
    "aws-ec2-placementgroup.json",
    "aws-organizations-account.json",
    "aws-ecr-repository.json",
    "aws-ses-dedicatedippool.json",
    "aws-iot-fleetmetric.json",
    "aws-appstream-fleet.json",
    "aws-mediaconnect-flowsource.json",
    "aws-greengrass-subscriptiondefinitionversion.json",
    "aws-lex-resourcepolicy.json",
    "aws-glue-registry.json",
    "aws-ec2-keypair.json",
    "aws-fsx-filesystem.json",
    "aws-appstream-applicationfleetassociation.json",
    "aws-ec2-eipassociation.json",
    "aws-elasticbeanstalk-application.json",
    "aws-iot-thingprincipalattachment.json",
    "aws-dlm-lifecyclepolicy.json",
    "aws-managedblockchain-accessor.json",
    "aws-ec2-capacityreservation.json",
    "aws-elasticloadbalancing-loadbalancer.json",
    "aws-transfer-user.json",
    "aws-cognito-identitypool.json",
    "aws-ec2-trafficmirrortarget.json",
    "aws-stepfunctions-statemachine.json",
    "aws-rds-dbclusterparametergroup.json",
    "aws-waf-xssmatchset.json",
    "aws-appmesh-virtualrouter.json",
    "aws-pinpoint-emailtemplate.json",
    "aws-appstream-directoryconfig.json",
    "aws-devopsguru-notificationchannel.json",
    "aws-codestar-githubrepository.json",
    "aws-inspector-assessmenttarget.json",
    "aws-fsx-snapshot.json",
    "aws-eventschemas-registrypolicy.json",
    "aws-route53-keysigningkey.json",
    "aws-eventschemas-registry.json",
    "aws-config-remediationconfiguration.json",
    "aws-greengrass-loggerdefinition.json",
    "aws-greengrass-devicedefinitionversion.json",
    "aws-events-connection.json",
    "aws-athena-datacatalog.json",
    "aws-docdb-dbcluster.json",
    "aws-mediaconnect-flowvpcinterface.json",
    "aws-greengrass-functiondefinitionversion.json",
    "aws-glue-workflow.json",
    "aws-apigatewayv2-authorizer.json",
    "aws-iot-accountauditconfiguration.json",
    "aws-sagemaker-userprofile.json",
    "aws-personalize-dataset.json",
    "aws-ec2-prefixlist.json",
    "aws-ec2-instance.json",
    "aws-networkmanager-device.json",
    "aws-ec2-subnetcidrblock.json",
    "aws-mediapackage-asset.json",
    "aws-elasticbeanstalk-applicationversion.json",
    "aws-appmesh-virtualgateway.json",
    "aws-waf-sqlinjectionmatchset.json",
    "aws-ec2-transitgatewayvpcattachment.json",
    "aws-ec2-flowlog.json",
    "aws-events-endpoint.json",
    "aws-amazonmq-broker.json",
    "aws-emr-step.json",
    "aws-ssm-association.json",
    "aws-ec2-clientvpnendpoint.json",
    "aws-cloudfront-responseheaderspolicy.json",
    "aws-guardduty-master.json",
    "aws-kms-alias.json",
    "aws-xray-samplingrule.json",
    "aws-route53resolver-resolverrule.json",
    "aws-transfer-connector.json",
    "aws-appmesh-virtualnode.json",
    "aws-apigateway-documentationversion.json",
    "aws-licensemanager-grant.json",
    "aws-wafv2-webaclassociation.json",
    "aws-oam-sink.json",
    "aws-codebuild-reportgroup.json",
    "aws-apigateway-gatewayresponse.json",
    "aws-ec2-clientvpnauthorizationrule.json",
    "aws-ec2-enclavecertificateiamroleassociation.json",
    "aws-connect-phonenumber.json",
    "aws-fsx-volume.json",
    "aws-acmpca-certificate.json",
    "aws-ec2-ipamallocation.json",
    "aws-workspaces-workspace.json",
    "aws-inspector-assessmenttemplate.json",
    "aws-emr-studio.json",
    "aws-directoryservice-microsoftad.json",
    "aws-memorydb-subnetgroup.json",
    "aws-datasync-locationobjectstorage.json",
    "aws-ecs-capacityprovider.json",
    "aws-elasticache-cachecluster.json",
    "aws-sagemaker-modelcard.json",
    "aws-logs-destination.json",
    "aws-eks-nodegroup.json",
    "aws-organizations-organizationalunit.json",
    "aws-appsync-datasource.json",
    "aws-sqs-queue.json",
    "aws-ec2-securitygroupingress.json",
    "aws-guardduty-detector.json",
    "aws-sagemaker-modelqualityjobdefinition.json",
    "aws-iot-provisioningtemplate.json",
    "aws-personalize-schema.json",
    "aws-appflow-flow.json",
    "aws-apigateway-stage.json",
    "aws-budgets-budget.json",
    "aws-batch-computeenvironment.json",
    "aws-connect-instancestorageconfig.json",
    "aws-iot-thing.json",
    "aws-route53-healthcheck.json",
    "aws-events-eventbuspolicy.json",
    "aws-athena-namedquery.json",
    "aws-ec2-trafficmirrorfilter.json",
    "aws-apigateway-deployment.json",
    "aws-wafregional-rule.json",
    "aws-inspector-resourcegroup.json",
    "aws-lakeformation-datalakesettings.json",
    "aws-greengrassv2-deployment.json",
    "aws-autoscaling-scalingpolicy.json",
    "aws-groundstation-config.json",
    "aws-resourceexplorer2-defaultviewassociation.json",
    "aws-ecr-registrypolicy.json",
    "aws-redshift-scheduledaction.json",
    "aws-rds-dbsecuritygroup.json",
    "aws-mediapackage-channel.json",
    "aws-apigatewayv2-routeresponse.json",
    "aws-cloudwatch-metricstream.json",
    "aws-ssm-parameter.json",
    "aws-apigatewayv2-apigatewaymanagedoverrides.json",
    "aws-config-deliverychannel.json",
    "aws-certificatemanager-account.json",
    "aws-sagemaker-monitoringschedule.json",
    "aws-iam-oidcprovider.json",
    "aws-lakeformation-tag.json",
    "aws-servicecatalogappregistry-resourceassociation.json",
    "aws-ec2-vpngateway.json",
    "aws-cloudformation-stack.json",
    "aws-resourcegroups-group.json",
    "aws-cloudformation-resourcedefaultversion.json",
    "aws-ssm-resourcedatasync.json",
    "aws-signer-profilepermission.json",
    "aws-docdb-dbclusterparametergroup.json",
    "aws-s3-multiregionaccesspoint.json",
    "aws-greengrass-loggerdefinitionversion.json",
    "aws-quicksight-dashboard.json",
    "aws-servicecatalog-tagoptionassociation.json",
    "aws-ec2-ipam.json",
    "aws-databrew-job.json",
    "aws-ec2-transitgatewaypeeringattachment.json",
    "aws-quicksight-template.json",
    "aws-cloudfront-cachepolicy.json",
    "aws-appintegrations-dataintegration.json",
    "aws-iam-accesskey.json",
    "aws-rds-dbsubnetgroup.json",
    "aws-ivschat-room.json",
    "aws-secretsmanager-secrettargetattachment.json",
    "aws-amazonmq-configuration.json",
    "aws-appconfig-deployment.json",
    "aws-codepipeline-customactiontype.json",
    "aws-accessanalyzer-analyzer.json",
    "aws-ec2-ec2fleet.json",
    "aws-pinpoint-inapptemplate.json",
    "aws-greengrass-resourcedefinition.json",
    "aws-dms-replicationinstance.json",
    "aws-servicecatalog-cloudformationproduct.json",
    "aws-s3-storagelens.json",
    "aws-iam-managedpolicy.json",
    "aws-ec2-launchtemplate.json",
    "aws-pinpoint-voicechannel.json",
    "aws-cloudfront-originrequestpolicy.json",
    "aws-datasync-locationfsxontap.json",
    "aws-networkmanager-linkassociation.json",
    "aws-cognito-userpoolriskconfigurationattachment.json",
    "aws-elasticbeanstalk-environment.json",
    "aws-cognito-userpoolclient.json",
    "aws-mediapackage-packaginggroup.json",
    "aws-wafregional-sqlinjectionmatchset.json",
    "aws-lambda-version.json",
    "aws-ec2-dhcpoptions.json",
    "aws-ec2-ipampool.json",
    "aws-kinesis-streamconsumer.json",
    "aws-iam-servicelinkedrole.json",
    "aws-cloudformation-hooktypeconfig.json",
    "aws-ec2-volume.json",
    "aws-licensemanager-license.json",
    "aws-iot-certificate.json",
    "aws-ec2-eip.json",
    "aws-greengrass-resourcedefinitionversion.json",
    "aws-cloudformation-resourceversion.json",
    "aws-sagemaker-modelexplainabilityjobdefinition.json",
    "aws-apigatewayv2-stage.json",
    "aws-chatbot-microsoftteamschannelconfiguration.json",
    "aws-rds-dbproxy.json",
    "aws-pinpoint-apnschannel.json",
    "aws-rds-dbparametergroup.json",
    "aws-securityhub-hub.json",
    "aws-s3-accesspoint.json",
    "aws-greengrass-groupversion.json",
    "aws-pinpoint-smschannel.json",
    "aws-ec2-trafficmirrorsession.json",
    "aws-s3outposts-bucketpolicy.json",
    "aws-batch-jobqueue.json",
    "aws-lightsail-alarm.json",
    "aws-redshift-eventsubscription.json",
    "aws-iotfleethub-application.json",
    "aws-ssmcontacts-contactchannel.json",
    "aws-memorydb-acl.json",
    "aws-cloudformation-waitconditionhandle.json",
    "aws-pinpoint-smstemplate.json",
    "aws-globalaccelerator-accelerator.json",
    "aws-eks-addon.json",
]
