# markdown_fate
architecture and source code analysis, also includes how to implement TEEP Usecase\
## purpose：怎样在fateflow中引入机密计算以及TEEP Usecase for confidential computing in network\
dag_scheduler? dag_scheduler introduced module information indeed, but then how?\
Job was distributed to tasks, which belong to Spark workflow. Fate needs to makesure every tasks was correctly deployed 
and runs in TEE environment?\
Simple situation: job was split to task, if job controller could make sure the task environment in Spark is trusted, then
it could transfer its data to tasks.\
How to verify if the job module or job algorithm is correctly deployed?\
Dag_scheduler and job_controller are very complicated method and class, how to decouple RA and scheduler, and re-use RA in
other FL project


# reference
https://wdxtub.com/flt/flt-c1/2021/07/02/
# fate1.9.1 在pycharm中调试：
## 1,首先使用github中的部署和运行命令把fateserver run起来：
  cd ${FATE_PROJECT_BASE};
  source bin/init_env.sh;
  cd fateflow;
  bash bin/service.sh status;
  bash bin/service.sh start
## 2,通过上述命令得到init_env.sh,里边有该项目所需的环境变量；通过在T中输入env，得到fate项目设置的环境变量
## 3，pycharm edit configuration，python下新建条目，将环境变量输入到environment中：
  EGGROLL_LOG_LEVEL=INFO]
  FATE_DEPLOY_BASE=/home/suede/1FATE/FATE
  FATE_LOG_LEVEL=DEBUG
  FATE_PROFILE_LOG_ENABLE=0
  FATE_PROJECT_BASE=/home/suede/1FATE/FATE
  FATE_VENV_BASE=/home/suede/fate_venv/fatevenv/
  PYTHONPATH=/home/suede/1FATE/FATE/python:/home/suede/1FATE/FATE/fateflow/python
  PYTHONUNBUFFERED=1
# fateflow基于flask实现，
fateflow server 通过start启动多线程
run_simple(apps)启动flask web server服务

## apps/
### __init__.py 
Flask 固定用法，在大项目中，使用此方法获得以模块形式存在的apps
### party_app和job_app的
party_app 对内，主要被scheduler调用？
job_app对外，主要被fateflow client调用？
#### job_app.py
submit_job()调用DAGScheduler.submit
#### party_app.py
party_app 通过create_job(job_id, role, party_id) 调用job_app产生的job_id
## scheduling_apps 
scheduling_apps/initiator_app.py 通过
  from fate_flow.scheduler.dag_scheduler import DAGScheduler
调用./scheduler 目录下的模块
## Scheduler 
### dag_scheduler.py
maybe：在dag_scheduler中插入关于module的远程证明信息
dsl通过.get()方法获得，get利用key在dict中获取值
job_app.py 会调用submit():@manager.route('/submit', methods=['POST'])
flask监听submit

run_do->schedule_waiting_jobs->cls.start_job 启动job,创建线程
    ->FederatedScheduler.start_job->job_command()
        -> t = threading.Thread(target=cls.federated_command, args=args)
           threads.append(t)
           t.start()

run_do->schedule_running_job 调度job,调度到以后启动线程 start_task
    ->TaskScheduler.schedule(job...)实际是task schedule
        ->start_task(job=job, task=waiting_task)
            ->FederatedScheduler.start_task(job,task) 
                ->status_code, response = cls.task_command(job=job, task=task, command="start", command_body={}, need_user=True)



1，运行的内容都由job class描述
    tbd1：job 只包括ta和pd，至于TEEP agent如何存在于task中，需要resource manager管理？
    解偶：resource manager负责建立cc environment，承载task，resource manager向
    tbd1:在job中增加对RA信息的描述，通过dsl分解后的RA信息也要描述，最好由可信第三方直接生成证书，
    tbd2：thread.start 信息如何包括RA
2，dsl是怎样将一个大应用分解的，通过dsl能够直接使用spark吗？

3，对进程和线程的需求，直接thread.start?
                    
这个过程是纯粹软件的过程，没有和硬件结合
### task_scheduler
dag_scheduler 和 task_scheduler 都调用federated_scheduler

### federated_scheduler

## utils/
### model_utils.py
model info in this file
### model_utils_ra.py
a new file maybe needed to add remote attestation information about model
this RA information using JWT format, but the item based on EAT: 
e.g. 
{
    / nonce /           10: h'948f8860d13a463e',
    / security-level / 261: 2, / restricted /
    / secure-boot /    262: true,
    / debug-status /   263: 2, / disabled-since-boot /
    / manfests /       273: [
                           [
                               121, / CoAP Content ID. A     /
                                    / made up one until one  /
                                    / is assigned for CoSWID /

                               / This is byte-string wrapped      /
                               / payload CoSWID. It gives the TEE /
                               / software name, the version and   /
                               / the  name of the file it is in.  /
                               / {0: "3a24",                      /
                               /  12: 1,                          /
                               /   1: "Acme TEE OS",              /
                               /  13: "3.1.4",                    /
                               /   2: [{31: "Acme TEE OS", 33: 1}, /
                               /       {31: "Acme TEE OS", 33: 2}], /
                               /   6: {                           /
                               /       17: {                      /
                               /           24: "acme_tee_3.exe"   /
                               /       }                          /
                               /    }                             /
                               /  }                               /
                               h' a60064336132340c01016b
                                  41636d6520544545204f530d65332e31
                                  2e340282a2181f6b41636d6520544545
                                  204f53182101a2181f6b41636d652054
                                  4545204f5318210206a111a118186e61
                                  636d655f7465655f332e657865'
                            ]
                        ]
}


TEEP agent:
RoT:
Hardware 
### dsl_parser.py
dsl是哪里来的
self._dsl = dsl if dsl else kwargs.get("job_dsl")
flow_client负责生成dsl,
make change mark




