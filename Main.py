
from pipeline_service import PipelineService

if __name__ == "__main__":
    print("Data Pipelines starts here")
    
    pipeline = PipelineService() # the part "PipelineService" is called in service notebook as class 
    pipeline.run()
    
    print("Data Pipelines ends here")
    
    