const fs = require('fs');

const setupDirs = () => {
  const dirs = ['frontend/src/api', 'frontend/src/components', 'frontend/src/pages'];
  dirs.forEach(dir => {
    if (!fs.existsSync(`D:/movie/sih/project/${dir}`)) {
      fs.mkdirSync(`D:/movie/sih/project/${dir}`, { recursive: true });
    }
  });
};

setupDirs();
