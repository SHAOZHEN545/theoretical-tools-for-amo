# Theoretical Tools for Atomic and Molecular Physics

An Obsidian knowledge base on the theoretical methods that come up again and again in atomic, molecular and optical physics experiments, published as a website:

**https://shaozhen545.github.io/theoretical-tools-for-amo/**

## Contents

- **Van Vleck perturbation theory**
  - [Van Vleck perturbation theory - near and far](Notes/Van%20Vleck%20perturbation%20theory/Van%20Vleck%20perturbation%20theory%20-%20near%20and%20far.md)
  - [Van Vleck perturbation theory and the effective Hamiltonian](Notes/Van%20Vleck%20perturbation%20theory/Van%20Vleck%20perturbation%20theory%20and%20the%20effective%20Hamiltonian.md)
  - [Van Vleck perturbation theory - dressed states and rotated operators](Notes/Van%20Vleck%20perturbation%20theory/Van%20Vleck%20perturbation%20theory%20-%20dressed%20states%20and%20rotated%20operators.md)
  - [Van Vleck perturbation theory - errors](Notes/Van%20Vleck%20perturbation%20theory/Van%20Vleck%20perturbation%20theory%20-%20errors.md)
  - [Van Vleck perturbation theory - symmetries](Notes/Van%20Vleck%20perturbation%20theory/Van%20Vleck%20perturbation%20theory%20-%20symmetries.md)

Numerical checks of the formulas are in [`checks/`](checks/). Run them from the repository root with Python 3 and NumPy, for example `python checks/check_van_vleck.py`. The scripts in [`figures/`](figures/) redraw the figures with Matplotlib, for example `python figures/van_vleck_block_diagonalization.py`; regenerating an unchanged figure leaves its SVG byte for byte the same.

## Open in Obsidian

Choose **Open folder as vault** and select this repository root. The included `.obsidian` folder supplies the editor configuration, shortcuts, plugins, and image styling. Enable community plugins when Obsidian asks if you trust this vault.

New notes default to `Notes/`; new attachments default to `Notes/Pictures/`. Each topic gets its own subfolder of `Notes/`.

## Included editing support

- **Callout Integrator**: add or remove blockquote prefixes with Ctrl+Shift+. and Ctrl+Shift+, on Windows.
- **Better Math in Callouts & Blockquotes**: improve math rendering in Live Preview.
- **Obsidian Git**: optional Git integration. Configure it after connecting the GitHub repository.
- **image-custom.css**: figure layout, image alignment, and small muted captions.

The image snippet uses `figure` callouts as containers. For example:

```markdown
> [!figure]
> ![[Two levels.svg|center|600]]
> A caption in the small, muted figure style.
```

Image aliases such as `center`, `left`, and `right` control alignment within figure callouts. Numeric dimensions control image size. Figure metadata such as `[!figure|center]` controls caption alignment.

## Website and automatic publishing

The website uses **Quartz 5.0.0 + GitHub Pages**, with the same setup as [scattering-theory-for-ultracold](https://github.com/SHAOZHEN545/scattering-theory-for-ultracold). Quartz reads `Notes/` directly, including its images and homepage `Notes/index.md`. There is no second copy of the notes to synchronize. The repository root remains the Obsidian vault.

### First publication (one time)

1. Create an empty public repository `theoretical-tools-for-amo` on GitHub, connect it as `origin`, and push `main`. Do not upload `node_modules/`, `public/` or the ignored caches; `.gitignore` excludes them.
2. Open the repository's **Settings → Pages**. Under **Build and deployment → Source**, select **GitHub Actions**.
3. Open **Actions**, select **Publish the notes** and wait for both `build` and `deploy` to succeed. If the first run preceded enabling Pages, choose **Run workflow** to rerun it.
4. Open the website address above. Until deployment succeeds, this address may return 404.

### Everyday editing

Edit and save the notes in Obsidian, then commit and push to `main`. GitHub Actions renders and publishes the latest pushed content. Local changes that have not been pushed are not yet on the website.

New notes and images under `Notes/` are picked up automatically. Add a link and a one-sentence description to `Notes/index.md` if a new note should also appear in the guide on the homepage. Notes marked `draft: true` in YAML frontmatter are excluded by Quartz.

The build validates note pages, internal links, heading anchors, local assets and MathJax errors before deploying. A failed build leaves the last successful website online; inspect the failed step under Actions.

### Local preview

With Node.js 24 and npm installed, run these commands from the repository root:

```sh
npm ci
npm run plugins
npm run preview
```

Open **http://localhost:8080**. The preview rebuilds when notes change. For a production check, run `npm run build` followed by `npm run verify` and `npm run verify:links`.

Quartz core is vendored in `quartz/` from the official `v5.0.0` release, with its MIT license in `QUARTZ_LICENSE.txt`. npm dependencies are locked in `package-lock.json`; Quartz plugins are pinned in `quartz.lock.json`. The figure and reading-column styles live in `quartz/styles/custom.scss`, and `scripts/adapt-quartz-plugins.mjs` adapts the pinned explorer, search and graph plugins to the GitHub project subpath. Renaming the GitHub repository later requires updating `configuration.baseUrl` and the footer link in `quartz.config.yaml`, the script links in the notes, and the links here.
