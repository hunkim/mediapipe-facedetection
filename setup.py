from setuptools import setup, find_packages

setup(
    name='mediapipe',
    version="0.0.1",
    url='https://github.com/google/mediapipe',
    description='MediaPipe is the simplest way for researchers and developers to build world-class ML solutions and applications for mobile, edge, cloud and the web.',
    author='The MediaPipe Authors',
    author_email='mediapipe@google.com',
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(
        exclude=['mediapipe.examples.desktop.*', 'mediapipe.model_maker.*']),
    cmdclass={
        'build_py': BuildPy,
        'build_modules': BuildModules,
        'build_ext': BuildExtension,
        'generate_metadata_schema': GenerateMetadataSchema,
        'gen_protos': GeneratePyProtos,
        'install': Install,
        'restore': Restore,
    },
    ext_modules=[
        BazelExtension('//mediapipe/python:_framework_bindings'),
        BazelExtension(
            '//mediapipe/tasks/cc/metadata/python:_pywrap_metadata_version'),
        BazelExtension(
            '//mediapipe/tasks/python/metadata/flatbuffers_lib:_pywrap_flatbuffers'
        ),
    ],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='Apache 2.0',
    keywords='mediapipe',
)
