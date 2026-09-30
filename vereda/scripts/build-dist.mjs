import { cp, mkdir, rm } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';

const root = path.resolve(process.cwd());
const dist = path.join(root, 'dist');

await rm(dist, { recursive: true, force: true });
await mkdir(dist, { recursive: true });

for (const file of ['index.html', 'styles.css', 'script.js']) {
  await cp(path.join(root, file), path.join(dist, file));
}

for (const directory of ['assets', 'lp', 'obrigado']) {
  await cp(path.join(root, directory), path.join(dist, directory), { recursive: true });
}

process.stdout.write(`Build estático preparado em ${dist}\n`);
