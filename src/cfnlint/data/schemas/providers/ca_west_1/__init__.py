from typing import List

# pylint: disable=too-many-lines
types = [
    "AWS::CDK::Metadata",
    "AWS::CE::AnomalySubscription",
    "AWS::Glue::Partition",
    "AWS::EC2::TransitGatewayRouteTablePropagation",
    "AWS::ApiGateway::BasePathMapping",
    "AWS::GuardDuty::Filter",
    "AWS::ECS::Service",
    "AWS::RAM::ResourceShare",
    "AWS::DMS::ReplicationConfig",
    "AWS::DynamoDB::Table",
    "AWS::EC2::SecurityGroupEgress",
    "AWS::Config::OrganizationConfigRule",
    "AWS::Glue::DataQualityRuleset",
    "AWS::Config::ConfigurationRecorder",
    "AWS::CloudFront::ContinuousDeploymentPolicy",
    "AWS::ECR::ReplicationConfiguration",
    "AWS::AppConfig::ExtensionAssociation",
    "AWS::EC2::IPAMPoolCidr",
    "AWS::Redshift::ClusterSubnetGroup",
    "AWS::RDS::DBInstance",
    "AWS::EC2::VPCDHCPOptionsAssociation",
    "AWS::ApiGateway::Model",
    "AWS::EC2::NetworkAcl",
    "AWS::Lambda::EventSourceMapping",
    "AWS::Logs::ResourcePolicy",
    "AWS::EC2::NetworkAclEntry",
    "AWS::ApiGateway::DocumentationPart",
    "AWS::CloudWatch::CompositeAlarm",
    "AWS::Route53Resolver::FirewallDomainList",
    "AWS::AppConfig::Application",
    "AWS::OpsWorks::Stack",
    "AWS::GameLift::Fleet",
    "AWS::GameLift::Build",
    "AWS::ApiGateway::RequestValidator",
    "AWS::AutoScaling::WarmPool",
    "AWS::ApplicationAutoScaling::ScalableTarget",
    "AWS::Config::StoredQuery",
    "AWS::ACMPCA::Permission",
    "AWS::ApiGateway::DomainName",
    "AWS::ECS::PrimaryTaskSet",
    "AWS::AutoScaling::AutoScalingGroup",
    "AWS::EKS::FargateProfile",
    "AWS::Route53::DNSSEC",
    "AWS::EC2::TransitGatewayRouteTable",
    "AWS::Route53::RecordSet",
    "AWS::EKS::AccessEntry",
    "AWS::ElastiCache::SecurityGroup",
    "AWS::OpsWorks::Layer",
    "AWS::KinesisFirehose::DeliveryStream",
    "AWS::ImageBuilder::Component",
    "AWS::Glue::Connection",
    "AWS::IAM::Group",
    "AWS::Organizations::ResourcePolicy",
    "AWS::EC2::TransitGatewayMulticastGroupSource",
    "AWS::GameLift::Alias",
    "AWS::ApiGateway::UsagePlanKey",
    "AWS::CloudFront::RealtimeLogConfig",
    "AWS::LakeFormation::DataCellsFilter",
    "AWS::DataSync::LocationHDFS",
    "AWS::EC2::VPCEndpointConnectionNotification",
    "AWS::CodePipeline::Pipeline",
    "AWS::OpsWorks::Instance",
    "AWS::Config::ConfigurationAggregator",
    "AWS::ImageBuilder::ImagePipeline",
    "AWS::ElasticLoadBalancingV2::ListenerCertificate",
    "AWS::Route53Resolver::ResolverRuleAssociation",
    "AWS::Synthetics::Canary",
    "AWS::SNS::Subscription",
    "AWS::EC2::NatGateway",
    "AWS::AppConfig::DeploymentStrategy",
    "AWS::Glue::DevEndpoint",
    "AWS::ElastiCache::UserGroup",
    "AWS::ImageBuilder::ImageRecipe",
    "AWS::ApiGateway::RestApi",
    "AWS::OpsWorks::ElasticLoadBalancerAttachment",
    "AWS::S3ObjectLambda::AccessPointPolicy",
    "AWS::ElastiCache::ReplicationGroup",
    "AWS::StepFunctions::StateMachineAlias",
    "AWS::Glue::Job",
    "AWS::Route53::HostedZone",
    "AWS::EKS::PodIdentityAssociation",
    "AWS::Glue::Table",
    "AWS::Logs::MetricFilter",
    "AWS::Lambda::Function",
    "AWS::SNS::Topic",
    "AWS::Backup::BackupSelection",
    "AWS::EC2::VPCGatewayAttachment",
    "AWS::CloudTrail::Trail",
    "AWS::EC2::VPNConnectionRoute",
    "AWS::EC2::InternetGateway",
    "AWS::EC2::GatewayRouteTableAssociation",
    "AWS::SSM::Document",
    "AWS::IAM::Role",
    "AWS::CloudFront::CloudFrontOriginAccessIdentity",
    "AWS::ApiGateway::ApiKey",
    "AWS::AutoScaling::LaunchConfiguration",
    "AWS::ApiGateway::ClientCertificate",
    "AWS::KinesisAnalyticsV2::Application",
    "AWS::Lambda::Alias",
    "AWS::WAF::IPSet",
    "AWS::EC2::TransitGatewayMulticastDomainAssociation",
    "AWS::WAF::SizeConstraintSet",
    "AWS::EC2::TransitGatewayRouteTableAssociation",
    "AWS::AppConfig::Environment",
    "AWS::ImageBuilder::Image",
    "AWS::ElastiCache::SecurityGroupIngress",
    "AWS::CloudWatch::Dashboard",
    "AWS::CloudWatch::Alarm",
    "AWS::GuardDuty::Member",
    "AWS::CloudFormation::CustomResource",
    "AWS::ElastiCache::ParameterGroup",
    "AWS::Glue::Classifier",
    "AWS::CodeDeploy::DeploymentGroup",
    "AWS::CloudFormation::StackSet",
    "AWS::EC2::Route",
    "AWS::CloudFormation::HookVersion",
    "AWS::XRay::ResourcePolicy",
    "AWS::DynamoDB::GlobalTable",
    "AWS::Backup::BackupPlan",
    "AWS::ImageBuilder::DistributionConfiguration",
    "AWS::LakeFormation::Permissions",
    "AWS::Glue::DataCatalogEncryptionSettings",
    "AWS::CloudFront::PublicKey",
    "AWS::RAM::Permission",
    "AWS::DataSync::Task",
    "AWS::ECS::TaskDefinition",
    "AWS::EC2::SpotFleet",
    "AWS::IoT::PolicyPrincipalAttachment",
    "AWS::S3::Bucket",
    "AWS::GuardDuty::IPSet",
    "AWS::ServiceDiscovery::HttpNamespace",
    "AWS::EMR::SecurityConfiguration",
    "AWS::CloudWatch::InsightRule",
    "AWS::ApiGateway::UsagePlan",
    "AWS::Batch::SchedulingPolicy",
    "AWS::Athena::WorkGroup",
    "AWS::IAM::ServerCertificate",
    "AWS::Events::EventBus",
    "AWS::Organizations::Organization",
    "AWS::SSM::MaintenanceWindowTarget",
    "AWS::ApiGateway::Authorizer",
    "AWS::IAM::Policy",
    "AWS::RDS::DBSecurityGroupIngress",
    "AWS::EC2::TransitGatewayMulticastGroupMember",
    "AWS::EC2::VolumeAttachment",
    "AWS::Glue::SecurityConfiguration",
    "AWS::ECS::ClusterCapacityProviderAssociations",
    "AWS::AppConfig::ConfigurationProfile",
    "AWS::Route53Resolver::FirewallRuleGroup",
    "AWS::EC2::TransitGateway",
    "AWS::EC2::VPCEndpointServicePermissions",
    "AWS::SSM::MaintenanceWindowTask",
    "AWS::EC2::TransitGatewayMulticastDomain",
    "AWS::EKS::Cluster",
    "AWS::EFS::FileSystem",
    "AWS::Logs::QueryDefinition",
    "AWS::IAM::InstanceProfile",
    "AWS::DataSync::LocationNFS",
    "AWS::CertificateManager::Certificate",
    "AWS::SDB::Domain",
    "AWS::EC2::SubnetRouteTableAssociation",
    "AWS::ImageBuilder::ContainerRecipe",
    "AWS::EFS::AccessPoint",
    "AWS::Redshift::ClusterSecurityGroupIngress",
    "AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::OpenSearchService::Domain",
    "AWS::ServiceDiscovery::Instance",
    "AWS::Elasticsearch::Domain",
    "AWS::EC2::NetworkInterfacePermission",
    "AWS::ServiceDiscovery::PrivateDnsNamespace",
    "AMZN::SDC::Deployment",
    "AWS::SecretsManager::ResourcePolicy",
    "AWS::CloudFormation::HookDefaultVersion",
    "AWS::Config::ConfigRule",
    "AWS::ImageBuilder::Workflow",
    "AWS::ECS::TaskSet",
    "AWS::ACMPCA::CertificateAuthorityActivation",
    "AWS::GuardDuty::ThreatIntelSet",
    "AWS::EC2::VPC",
    "AWS::ARCZonalShift::ZonalAutoshiftConfiguration",
    "AWS::DataSync::LocationAzureBlob",
    "AWS::Logs::LogStream",
    "AWS::Route53::RecordSetGroup",
    "AWS::CloudFormation::PublicTypeVersion",
    "AWS::OpsWorks::App",
    "AWS::Kinesis::Stream",
    "AWS::Batch::JobDefinition",
    "AWS::IAM::SAMLProvider",
    "AWS::CloudFront::KeyGroup",
    "AWS::EC2::NetworkInterfaceAttachment",
    "AWS::EC2::TransitGatewayAttachment",
    "AWS::Glue::CustomEntityType",
    "AWS::CodeDeploy::DeploymentConfig",
    "AWS::StepFunctions::StateMachineVersion",
    "AWS::ServiceCatalogAppRegistry::Application",
    "AWS::Glue::Database",
    "AWS::Backup::BackupVault",
    "AWS::EC2::CustomerGateway",
    "AWS::IAM::GroupPolicy",
    "AWS::WAF::ByteMatchSet",
    "AWS::EC2::Host",
    "AWS::EC2::RouteTable",
    "AWS::DataSync::LocationSMB",
    "AWS::SecurityHub::Standard",
    "AWS::SNS::TopicInlinePolicy",
    "AWS::Redshift::ClusterParameterGroup",
    "AWS::Organizations::Policy",
    "AWS::Glue::Trigger",
    "AWS::EC2::VPCPeeringConnection",
    "AWS::SNS::TopicPolicy",
    "AWS::KMS::Key",
    "AWS::Route53Resolver::ResolverDNSSECConfig",
    "AWS::Route53Resolver::FirewallRuleGroupAssociation",
    "AWS::Route53Resolver::ResolverQueryLoggingConfig",
    "AWS::EC2::SnapshotBlockPublicAccess",
    "AWS::EC2::Subnet",
    "AWS::S3ObjectLambda::AccessPoint",
    "AWS::WAF::Rule",
    "AWS::ElasticBeanstalk::ConfigurationTemplate",
    "AWS::SQS::QueuePolicy",
    "AWS::ApiGateway::Account",
    "AWS::EC2::SecurityGroup",
    "AWS::EC2::CapacityReservationFleet",
    "AWS::OpsWorks::Volume",
    "AWS::IAM::UserToGroupAddition",
    "AWS::Events::Rule",
    "AWS::CloudFront::KeyValueStore",
    "AWS::EC2::VPNGatewayRoutePropagation",
    "AWS::Glue::Crawler",
    "AWS::CloudFront::Function",
    "AWS::ApiGateway::Method",
    "AWS::SSM::PatchBaseline",
    "AWS::ServiceDiscovery::Service",
    "AWS::CloudFront::MonitoringSubscription",
    "AWS::EFS::MountTarget",
    "AWS::EC2::VPNConnection",
    "AWS::WAF::WebACL",
    "AWS::ServiceDiscovery::PublicDnsNamespace",
    "AWS::IAM::User",
    "AWS::EMR::InstanceGroupConfig",
    "AWS::StepFunctions::Activity",
    "AWS::S3::BucketPolicy",
    "AWS::Redshift::Cluster",
    "AWS::EMR::InstanceFleetConfig",
    "AWS::EMR::Cluster",
    "AWS::RDS::DBCluster",
    "AWS::CloudFront::Distribution",
    "AWS::ElastiCache::SubnetGroup",
    "AWS::XRay::Group",
    "AWS::Oam::Link",
    "AWS::KMS::ReplicaKey",
    "AWS::Redshift::ClusterSecurityGroup",
    "AWS::ECR::PullThroughCacheRule",
    "AWS::Glue::MLTransform",
    "AWS::AppConfig::HostedConfigurationVersion",
    "AWS::DataSync::LocationEFS",
    "AWS::ApiGateway::Resource",
    "AWS::ElasticLoadBalancingV2::TargetGroup",
    "AWS::ApplicationAutoScaling::ScalingPolicy",
    "AWS::CloudFormation::Macro",
    "AWS::Lambda::LayerVersionPermission",
    "AWS::SecretsManager::Secret",
    "AWS::Route53Resolver::ResolverConfig",
    "AWS::ElastiCache::User",
    "AWS::Logs::SubscriptionFilter",
    "AWS::CodeDeploy::Application",
    "AWS::IoT::TopicRule",
    "AWS::LakeFormation::PrincipalPermissions",
    "AWS::DataSync::LocationS3",
    "AWS::AutoScaling::LifecycleHook",
    "AWS::EC2::NetworkInterface",
    "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation",
    "AWS::Lambda::EventInvokeConfig",
    "AWS::Lambda::LayerVersion",
    "AWS::RDS::OptionGroup",
    "AWS::OpsWorks::UserProfile",
    "AWS::IoT::Policy",
    "AWS::EC2::TransitGatewayRoute",
    "AWS::SSM::MaintenanceWindow",
    "AWS::LakeFormation::TagAssociation",
    "AWS::EC2::IPAMResourceDiscovery",
    "AWS::ImageBuilder::InfrastructureConfiguration",
    "AWS::CloudFormation::WaitCondition",
    "AWS::Route53Resolver::ResolverEndpoint",
    "AWS::CloudWatch::AnomalyDetector",
    "AWS::EC2::SubnetNetworkAclAssociation",
    "AWS::IAM::UserPolicy",
    "AWS::CloudFront::OriginAccessControl",
    "AWS::SecretsManager::RotationSchedule",
    "AWS::Lambda::Permission",
    "AWS::EKS::IdentityProviderConfig",
    "AWS::EC2::IPAMResourceDiscoveryAssociation",
    "AWS::ServiceCatalogAppRegistry::AttributeGroup",
    "AWS::EC2::EgressOnlyInternetGateway",
    "AWS::EC2::VPCCidrBlock",
    "AWS::ACMPCA::CertificateAuthority",
    "AWS::Athena::PreparedStatement",
    "AWS::AutoScaling::ScheduledAction",
    "AWS::LakeFormation::Resource",
    "AWS::EC2::IPAMScope",
    "AWS::DirectoryService::SimpleAD",
    "AWS::EC2::VPCEndpoint",
    "AWS::RDS::EventSubscription",
    "AWS::Config::AggregationAuthorization",
    "AWS::DataSync::Agent",
    "AWS::Logs::LogGroup",
    "AWS::ECS::Cluster",
    "AWS::EC2::PlacementGroup",
    "AWS::Organizations::Account",
    "AWS::ECR::Repository",
    "AWS::AppConfig::Extension",
    "AWS::ElasticLoadBalancingV2::ListenerRule",
    "AWS::EC2::KeyPair",
    "AWS::EC2::EIPAssociation",
    "AWS::ElasticBeanstalk::Application",
    "AWS::IoT::ThingPrincipalAttachment",
    "AWS::DLM::LifecyclePolicy",
    "AWS::EC2::CapacityReservation",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::IAM::RolePolicy",
    "AWS::StepFunctions::StateMachine",
    "AWS::RDS::DBClusterParameterGroup",
    "AWS::WAF::XssMatchSet",
    "AWS::Route53::KeySigningKey",
    "AWS::Config::RemediationConfiguration",
    "AWS::Athena::DataCatalog",
    "AWS::Glue::Workflow",
    "AWS::EC2::PrefixList",
    "AWS::EC2::Instance",
    "AWS::EC2::SubnetCidrBlock",
    "AWS::ElasticBeanstalk::ApplicationVersion",
    "AWS::WAF::SqlInjectionMatchSet",
    "AWS::EC2::TransitGatewayVpcAttachment",
    "AWS::EC2::FlowLog",
    "AWS::EMR::Step",
    "AWS::SSM::Association",
    "AWS::CloudFront::ResponseHeadersPolicy",
    "AWS::SecurityHub::AutomationRule",
    "AWS::GuardDuty::Master",
    "AWS::KMS::Alias",
    "AWS::XRay::SamplingRule",
    "AWS::Route53Resolver::ResolverRule",
    "AWS::ApiGateway::DocumentationVersion",
    "AWS::Oam::Sink",
    "AWS::ApiGateway::GatewayResponse",
    "AWS::ACMPCA::Certificate",
    "AWS::EC2::IPAMAllocation",
    "AWS::WorkSpaces::Workspace",
    "AWS::DirectoryService::MicrosoftAD",
    "AWS::DataSync::LocationObjectStorage",
    "AWS::ECS::CapacityProvider",
    "AWS::ElastiCache::CacheCluster",
    "AWS::SageMaker::ModelCard",
    "AWS::Logs::Destination",
    "AWS::EKS::Nodegroup",
    "AWS::Organizations::OrganizationalUnit",
    "AWS::SQS::Queue",
    "AWS::EC2::SecurityGroupIngress",
    "AWS::GuardDuty::Detector",
    "AWS::ApiGateway::Stage",
    "AWS::Batch::ComputeEnvironment",
    "AWS::DataPipeline::Pipeline",
    "AWS::IoT::Thing",
    "AWS::Route53::HealthCheck",
    "AWS::Events::EventBusPolicy",
    "AWS::Athena::NamedQuery",
    "AWS::ApiGateway::Deployment",
    "AWS::LakeFormation::DataLakeSettings",
    "AWS::AutoScaling::ScalingPolicy",
    "AWS::ECR::RegistryPolicy",
    "AWS::RDS::DBSecurityGroup",
    "AWS::CloudWatch::MetricStream",
    "AWS::SSM::Parameter",
    "AWS::Config::DeliveryChannel",
    "AWS::IAM::OIDCProvider",
    "AWS::LakeFormation::Tag",
    "AWS::CE::AnomalyMonitor",
    "AWS::ServiceCatalogAppRegistry::ResourceAssociation",
    "AWS::EC2::VPNGateway",
    "AWS::CloudFormation::Stack",
    "AWS::ResourceGroups::Group",
    "AWS::CloudFormation::ResourceDefaultVersion",
    "AWS::SSM::ResourceDataSync",
    "AWS::EC2::IPAM",
    "AWS::EC2::TransitGatewayPeeringAttachment",
    "AWS::CloudFront::CachePolicy",
    "AWS::IAM::AccessKey",
    "AWS::RDS::DBSubnetGroup",
    "AWS::SecretsManager::SecretTargetAttachment",
    "AWS::AppConfig::Deployment",
    "AWS::CodePipeline::CustomActionType",
    "AWS::AccessAnalyzer::Analyzer",
    "AWS::EC2::EC2Fleet",
    "AWS::EC2::VPCEndpointService",
    "AWS::IAM::ManagedPolicy",
    "AWS::EC2::LaunchTemplate",
    "AWS::CloudFront::OriginRequestPolicy",
    "AWS::ElasticBeanstalk::Environment",
    "AWS::Lambda::Version",
    "AWS::EC2::DHCPOptions",
    "AWS::EC2::IPAMPool",
    "AWS::Kinesis::StreamConsumer",
    "AWS::IAM::ServiceLinkedRole",
    "AWS::CloudFormation::HookTypeConfig",
    "AWS::EC2::Volume",
    "AWS::IoT::Certificate",
    "AWS::EC2::EIP",
    "AWS::CloudFormation::ResourceVersion",
    "AWS::RDS::DBParameterGroup",
    "AWS::SecurityHub::Hub",
    "AWS::S3::AccessPoint",
    "AWS::Batch::JobQueue",
    "AWS::ElasticLoadBalancingV2::Listener",
    "AWS::CloudFormation::WaitConditionHandle",
    "AWS::EKS::Addon",
]

# pylint: disable=too-many-lines
cached: List[str] = [
    "aws-ce-anomalysubscription.json",
    "aws-glue-partition.json",
    "aws-guardduty-filter.json",
    "aws-ecs-service.json",
    "aws-ram-resourceshare.json",
    "aws-dms-replicationconfig.json",
    "aws-ec2-securitygroupegress.json",
    "aws-config-organizationconfigrule.json",
    "aws-glue-dataqualityruleset.json",
    "aws-config-configurationrecorder.json",
    "aws-cloudfront-continuousdeploymentpolicy.json",
    "aws-ecr-replicationconfiguration.json",
    "aws-appconfig-extensionassociation.json",
    "aws-ec2-ipampoolcidr.json",
    "aws-rds-dbinstance.json",
    "aws-ec2-vpcdhcpoptionsassociation.json",
    "aws-ec2-networkacl.json",
    "aws-logs-resourcepolicy.json",
    "aws-cloudwatch-compositealarm.json",
    "aws-route53resolver-firewalldomainlist.json",
    "aws-appconfig-application.json",
    "aws-autoscaling-warmpool.json",
    "aws-config-storedquery.json",
    "aws-acmpca-permission.json",
    "aws-ecs-primarytaskset.json",
    "aws-autoscaling-autoscalinggroup.json",
    "aws-eks-fargateprofile.json",
    "aws-route53-dnssec.json",
    "aws-ec2-transitgatewayroutetable.json",
    "aws-route53-recordset.json",
    "aws-eks-accessentry.json",
    "aws-elasticache-securitygroup.json",
    "aws-kinesisfirehose-deliverystream.json",
    "aws-imagebuilder-component.json",
    "aws-glue-connection.json",
    "aws-organizations-resourcepolicy.json",
    "aws-ec2-transitgatewaymulticastgroupsource.json",
    "aws-cloudfront-realtimelogconfig.json",
    "aws-lakeformation-datacellsfilter.json",
    "aws-datasync-locationhdfs.json",
    "aws-ec2-vpcendpointconnectionnotification.json",
    "aws-codepipeline-pipeline.json",
    "aws-config-configurationaggregator.json",
    "aws-imagebuilder-imagepipeline.json",
    "aws-elasticloadbalancingv2-listenercertificate.json",
    "aws-route53resolver-resolverruleassociation.json",
    "aws-synthetics-canary.json",
    "aws-sns-subscription.json",
    "aws-ec2-natgateway.json",
    "aws-appconfig-deploymentstrategy.json",
    "aws-glue-devendpoint.json",
    "aws-imagebuilder-imagerecipe.json",
    "aws-opsworks-elasticloadbalancerattachment.json",
    "aws-s3objectlambda-accesspointpolicy.json",
    "aws-elasticache-replicationgroup.json",
    "aws-stepfunctions-statemachinealias.json",
    "aws-glue-job.json",
    "aws-eks-podidentityassociation.json",
    "aws-glue-table.json",
    "aws-logs-metricfilter.json",
    "aws-lambda-function.json",
    "aws-sns-topic.json",
    "aws-backup-backupselection.json",
    "aws-cloudtrail-trail.json",
    "aws-ec2-internetgateway.json",
    "aws-ec2-gatewayroutetableassociation.json",
    "aws-cloudfront-cloudfrontoriginaccessidentity.json",
    "aws-kinesisanalyticsv2-application.json",
    "aws-lambda-alias.json",
    "aws-ec2-transitgatewaymulticastdomainassociation.json",
    "aws-appconfig-environment.json",
    "aws-imagebuilder-image.json",
    "aws-elasticache-securitygroupingress.json",
    "aws-cloudwatch-dashboard.json",
    "aws-guardduty-member.json",
    "aws-cloudformation-customresource.json",
    "aws-elasticache-parametergroup.json",
    "aws-glue-classifier.json",
    "aws-codedeploy-deploymentgroup.json",
    "aws-cloudformation-stackset.json",
    "aws-ec2-route.json",
    "aws-cloudformation-hookversion.json",
    "aws-xray-resourcepolicy.json",
    "aws-backup-backupplan.json",
    "aws-imagebuilder-distributionconfiguration.json",
    "aws-lakeformation-permissions.json",
    "aws-glue-datacatalogencryptionsettings.json",
    "aws-cloudfront-publickey.json",
    "aws-ram-permission.json",
    "aws-datasync-task.json",
    "aws-ecs-taskdefinition.json",
    "aws-ec2-spotfleet.json",
    "aws-s3-bucket.json",
    "aws-guardduty-ipset.json",
    "aws-servicediscovery-httpnamespace.json",
    "aws-cloudwatch-insightrule.json",
    "aws-batch-schedulingpolicy.json",
    "aws-athena-workgroup.json",
    "aws-iam-servercertificate.json",
    "aws-organizations-organization.json",
    "aws-ssm-maintenancewindowtarget.json",
    "aws-rds-dbsecuritygroupingress.json",
    "aws-glue-securityconfiguration.json",
    "aws-ecs-clustercapacityproviderassociations.json",
    "aws-appconfig-configurationprofile.json",
    "aws-route53resolver-firewallrulegroup.json",
    "aws-ec2-transitgateway.json",
    "aws-ec2-vpcendpointservicepermissions.json",
    "aws-ssm-maintenancewindowtask.json",
    "aws-ec2-transitgatewaymulticastdomain.json",
    "aws-eks-cluster.json",
    "aws-efs-filesystem.json",
    "aws-logs-querydefinition.json",
    "aws-datasync-locationnfs.json",
    "aws-certificatemanager-certificate.json",
    "aws-sdb-domain.json",
    "aws-ec2-subnetroutetableassociation.json",
    "aws-imagebuilder-containerrecipe.json",
    "aws-efs-accesspoint.json",
    "aws-redshift-clustersecuritygroupingress.json",
    "aws-servicecatalogappregistry-attributegroupassociation.json",
    "aws-elasticloadbalancingv2-loadbalancer.json",
    "aws-opensearchservice-domain.json",
    "aws-servicediscovery-instance.json",
    "aws-elasticsearch-domain.json",
    "aws-servicediscovery-privatednsnamespace.json",
    "aws-secretsmanager-resourcepolicy.json",
    "aws-cloudformation-hookdefaultversion.json",
    "aws-imagebuilder-workflow.json",
    "aws-ecs-taskset.json",
    "aws-acmpca-certificateauthorityactivation.json",
    "aws-guardduty-threatintelset.json",
    "aws-ec2-vpc.json",
    "aws-arczonalshift-zonalautoshiftconfiguration.json",
    "aws-datasync-locationazureblob.json",
    "aws-logs-logstream.json",
    "aws-route53-recordsetgroup.json",
    "aws-cloudformation-publictypeversion.json",
    "aws-opsworks-app.json",
    "aws-kinesis-stream.json",
    "aws-iam-samlprovider.json",
    "aws-cloudfront-keygroup.json",
    "aws-ec2-networkinterfaceattachment.json",
    "aws-glue-customentitytype.json",
    "aws-codedeploy-deploymentconfig.json",
    "aws-stepfunctions-statemachineversion.json",
    "aws-servicecatalogappregistry-application.json",
    "aws-glue-database.json",
    "aws-backup-backupvault.json",
    "aws-iam-grouppolicy.json",
    "aws-waf-bytematchset.json",
    "aws-ec2-routetable.json",
    "aws-datasync-locationsmb.json",
    "aws-securityhub-standard.json",
    "aws-sns-topicinlinepolicy.json",
    "aws-organizations-policy.json",
    "aws-glue-trigger.json",
    "aws-ec2-vpcpeeringconnection.json",
    "aws-sns-topicpolicy.json",
    "aws-kms-key.json",
    "aws-route53resolver-resolverdnssecconfig.json",
    "aws-route53resolver-firewallrulegroupassociation.json",
    "aws-route53resolver-resolverqueryloggingconfig.json",
    "aws-ec2-snapshotblockpublicaccess.json",
    "aws-ec2-subnet.json",
    "aws-s3objectlambda-accesspoint.json",
    "aws-sqs-queuepolicy.json",
    "aws-ec2-securitygroup.json",
    "aws-ec2-capacityreservationfleet.json",
    "aws-opsworks-volume.json",
    "aws-iam-usertogroupaddition.json",
    "aws-events-rule.json",
    "aws-cloudfront-keyvaluestore.json",
    "aws-cloudfront-function.json",
    "aws-ssm-patchbaseline.json",
    "aws-servicediscovery-service.json",
    "aws-cloudfront-monitoringsubscription.json",
    "aws-efs-mounttarget.json",
    "aws-servicediscovery-publicdnsnamespace.json",
    "aws-emr-instancegroupconfig.json",
    "aws-s3-bucketpolicy.json",
    "aws-emr-instancefleetconfig.json",
    "aws-emr-cluster.json",
    "aws-rds-dbcluster.json",
    "aws-cloudfront-distribution.json",
    "aws-xray-group.json",
    "aws-oam-link.json",
    "aws-kms-replicakey.json",
    "aws-redshift-clustersecuritygroup.json",
    "aws-ecr-pullthroughcacherule.json",
    "aws-glue-mltransform.json",
    "aws-appconfig-hostedconfigurationversion.json",
    "aws-datasync-locationefs.json",
    "aws-elasticloadbalancingv2-targetgroup.json",
    "aws-cloudformation-macro.json",
    "aws-lambda-layerversionpermission.json",
    "aws-secretsmanager-secret.json",
    "aws-route53resolver-resolverconfig.json",
    "aws-logs-subscriptionfilter.json",
    "aws-codedeploy-application.json",
    "aws-lakeformation-principalpermissions.json",
    "aws-datasync-locations3.json",
    "aws-ec2-networkinterface.json",
    "aws-route53resolver-resolverqueryloggingconfigassociation.json",
    "aws-lambda-eventinvokeconfig.json",
    "aws-lambda-layerversion.json",
    "aws-rds-optiongroup.json",
    "aws-opsworks-userprofile.json",
    "aws-ssm-maintenancewindow.json",
    "aws-lakeformation-tagassociation.json",
    "aws-ec2-ipamresourcediscovery.json",
    "aws-imagebuilder-infrastructureconfiguration.json",
    "aws-route53resolver-resolverendpoint.json",
    "aws-cloudwatch-anomalydetector.json",
    "aws-iam-userpolicy.json",
    "aws-cloudfront-originaccesscontrol.json",
    "aws-secretsmanager-rotationschedule.json",
    "aws-lambda-permission.json",
    "aws-eks-identityproviderconfig.json",
    "aws-ec2-ipamresourcediscoveryassociation.json",
    "aws-servicecatalogappregistry-attributegroup.json",
    "aws-ec2-egressonlyinternetgateway.json",
    "aws-acmpca-certificateauthority.json",
    "aws-athena-preparedstatement.json",
    "aws-lakeformation-resource.json",
    "aws-ec2-ipamscope.json",
    "aws-rds-eventsubscription.json",
    "aws-config-aggregationauthorization.json",
    "aws-datasync-agent.json",
    "aws-logs-loggroup.json",
    "aws-ecs-cluster.json",
    "aws-ec2-placementgroup.json",
    "aws-organizations-account.json",
    "aws-ecr-repository.json",
    "aws-appconfig-extension.json",
    "aws-elasticloadbalancingv2-listenerrule.json",
    "aws-ec2-keypair.json",
    "aws-ec2-eipassociation.json",
    "aws-dlm-lifecyclepolicy.json",
    "aws-ec2-capacityreservation.json",
    "aws-elasticloadbalancing-loadbalancer.json",
    "aws-iam-rolepolicy.json",
    "aws-rds-dbclusterparametergroup.json",
    "aws-route53-keysigningkey.json",
    "aws-config-remediationconfiguration.json",
    "aws-athena-datacatalog.json",
    "aws-glue-workflow.json",
    "aws-ec2-prefixlist.json",
    "aws-waf-sqlinjectionmatchset.json",
    "aws-ec2-transitgatewayvpcattachment.json",
    "aws-ec2-flowlog.json",
    "aws-ssm-association.json",
    "aws-cloudfront-responseheaderspolicy.json",
    "aws-securityhub-automationrule.json",
    "aws-guardduty-master.json",
    "aws-kms-alias.json",
    "aws-xray-samplingrule.json",
    "aws-route53resolver-resolverrule.json",
    "aws-oam-sink.json",
    "aws-acmpca-certificate.json",
    "aws-ec2-ipamallocation.json",
    "aws-workspaces-workspace.json",
    "aws-datasync-locationobjectstorage.json",
    "aws-ecs-capacityprovider.json",
    "aws-elasticache-cachecluster.json",
    "aws-sagemaker-modelcard.json",
    "aws-logs-destination.json",
    "aws-eks-nodegroup.json",
    "aws-organizations-organizationalunit.json",
    "aws-sqs-queue.json",
    "aws-guardduty-detector.json",
    "aws-batch-computeenvironment.json",
    "aws-events-eventbuspolicy.json",
    "aws-athena-namedquery.json",
    "aws-lakeformation-datalakesettings.json",
    "aws-ecr-registrypolicy.json",
    "aws-rds-dbsecuritygroup.json",
    "aws-cloudwatch-metricstream.json",
    "aws-ssm-parameter.json",
    "aws-config-deliverychannel.json",
    "aws-iam-oidcprovider.json",
    "aws-lakeformation-tag.json",
    "aws-ce-anomalymonitor.json",
    "aws-servicecatalogappregistry-resourceassociation.json",
    "aws-resourcegroups-group.json",
    "aws-cloudformation-resourcedefaultversion.json",
    "aws-ec2-ipam.json",
    "aws-ec2-transitgatewaypeeringattachment.json",
    "aws-cloudfront-cachepolicy.json",
    "aws-rds-dbsubnetgroup.json",
    "aws-appconfig-deployment.json",
    "aws-accessanalyzer-analyzer.json",
    "aws-ec2-ec2fleet.json",
    "aws-ec2-vpcendpointservice.json",
    "aws-ec2-launchtemplate.json",
    "aws-cloudfront-originrequestpolicy.json",
    "aws-ec2-dhcpoptions.json",
    "aws-ec2-ipampool.json",
    "aws-iam-servicelinkedrole.json",
    "aws-cloudformation-hooktypeconfig.json",
    "aws-ec2-eip.json",
    "aws-cloudformation-resourceversion.json",
    "aws-rds-dbparametergroup.json",
    "aws-securityhub-hub.json",
    "aws-s3-accesspoint.json",
    "aws-batch-jobqueue.json",
    "aws-elasticloadbalancingv2-listener.json",
    "aws-cloudformation-waitconditionhandle.json",
    "aws-eks-addon.json",
]
