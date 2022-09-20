# markdown_fate
architecture and source code analysis, also includes how to implement TEEP Usecase

fate1.9.1 在pycharm中调试：
1,首先使用github中的部署和运行命令把fateserver run起来：
  cd ${FATE_PROJECT_BASE};
  source bin/init_env.sh;
  cd fateflow;
  bash bin/service.sh status;
  bash bin/service.sh start
2,通过上述命令得到init_env.sh,里边有该项目所需的环境变量；通过在T中输入env，得到fate项目设置的环境变量
3，pycharm edit configuration，python下新建条目，将环境变量输入到environment中：
  EGGROLL_LOG_LEVEL=INFO]
  FATE_DEPLOY_BASE=/home/suede/1FATE/FATE
  FATE_LOG_LEVEL=DEBUG
  FATE_PROFILE_LOG_ENABLE=0
  FATE_PROJECT_BASE=/home/suede/1FATE/FATE
  FATE_VENV_BASE=/home/suede/fate_venv/fatevenv/
  PYTHONPATH=/home/suede/1FATE/FATE/python:/home/suede/1FATE/FATE/fateflow/python
  PYTHONUNBUFFERED=1
