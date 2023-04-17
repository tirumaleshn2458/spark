def run():

    try:
        import pyspark.tensorflow
    except:
        import os
        try:
            import tensorflow
        except:
            os.system('pip install tensorflow')
        import tensorflow
        tensorflow_path = os.path.dirname(tensorflow.__file__)
        import pyspark
        source_path = os.path.dirname(pyspark.__file__)

        ts_folder = "tensorflow"

        #try:
        tensorflow_source_path=os.path.join(source_path,ts_folder)
        #except:
        #    pass

        import shutil

        if True:
            print('Tensorflow is installing')
            shutil.copytree(tensorflow_path,tensorflow_source_path)
        else:
            pass
