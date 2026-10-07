variable "aws_region" {
    description = "AWS 리전"
    type = string
    default = "us_east-1"
}

# AWS 리소스간 공통 prefix
variable "project_name" {
    description = "프로젝트별 구분값"
    type = string
    default = "agent-de-ai-08"
}

# VPC 대역
variable "vpc_cidr" {
    description = "VPC CIDR"
    type = string
    default = "10.30.0.0/15"
}

# EC2 관련
# Agent/fastapi
variable "ec2_instance_type" {
    description = "에이전트 구동용 EC2"
    type = string
    default = "t3.micro"
}

# RDS내 DB명
variable "db_name" {
  description = "백터 DB명"
  type = string
  default = "agentlab"
}

# RDS내 사용자명
variable "db_username" {
  description = "백터 DB 접근 사용자명"
  type = string
  default = "agent"
}

# RDS내 비밀번호
variable "db_password" {
  description = "RDS 마스터 패스워드"
  type = string
  sensitive = true
}

# RDS 인스턴스 사양
variable "db_instance_class" {
  description = "RDS 인스턴스 유형"
  type = string
  default = "db.t4g.micro"
}

# PostgreSQL 엔진 버전
variable "postgre_version" {
  description = "엔진 버전"
  type = string
  default = "16"
}

# Bedrock Model Id
variable "chat_model" {
  description = "엔트로픽 기본 모델"
  type = string
  # Agent가 사용하는 claude 모델, 리전이 변경되면 'us' 부분도 변경
  default = "us.anthropic.claude-sonnet-5"
}

# 임베딩 모델
variable "embed_model" {
  description = "임베딩 모델"
  type = string
  default = "amazon.titan-embed-text-v2:0"
}

# Agent Memory에 대한 기본 사용자 ID
variable "user_id" {
  description = "임시 사용자 ID"
  type = string
  default = "demo-user-08"
}

# FastAPI (8000) 접속 IP cidr
# 편의상 전체 개방
variable "api_cidr" {
    description = "FastAPI용 CIDR"
    type = string
    default = "0.0.0.0/0"
}

# SSH 관련 