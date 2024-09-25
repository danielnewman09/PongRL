from pathlib import Path
from conan import ConanFile
from conan.tools.files import copy

local_script_abs_path = Path(__file__)
_WORKSPACE_ROOT_DIR = local_script_abs_path.parent.absolute()

class PongRLConan(ConanFile):
    
    name = "pongRL"
    version = "0.0"
    author = "Daniel M Newman"
    description = "Handle PongRL dependencies"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain"
    
    def requirements(self):
        self.requires("sfml/2.6.1")
        
    def generate(self):
        for dep in self.dependencies.values():
            
            if len(dep.cpp_info.libdirs) > 0:
                installs_dir = _WORKSPACE_ROOT_DIR.joinpath('./installs/')
                copy(self, "*",dep.cpp_info.libdirs[0], dst=installs_dir.absolute(),  excludes=('conaninfo*', 'conanmanifest*'))
                