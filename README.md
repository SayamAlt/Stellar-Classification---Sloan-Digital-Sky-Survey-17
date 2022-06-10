# Stellar-Classification : Sloan-Digital-Sky-Survey-17

![Stars and Galaxies](https://media2.giphy.com/media/OYfQ5c7FPeBxe/giphy.gif)
![Stellar Classification](https://scitechdaily.com/images/Primordial-Stellar-Stream-Near-Milky-Way-scaled.jpg)
![Stellar](https://s3.envato.com/files/196219035/stellar_space_preview.jpg)

## Deployed Web Application

Link: https://stellar-classification.herokuapp.com/

## Context 

<p>In astronomy, stellar classification is the classification of stars based on their spectral characteristics. The classification scheme of galaxies, quasars, and stars is one of the most fundamental in astronomy. The early cataloguing of stars and their distribution in the sky has led to the understanding that they make up our own galaxy and, following the distinction that Andromeda was a separate galaxy to our own, numerous galaxies began to be surveyed as more powerful telescopes were built. This datasat aims to classify stars, galaxies, and quasars based on their spectral characteristics.</p>

<table>
  <tr>
    <th><b>Stellar Object</b></th>
    <th><b>Description</b></th>
  </tr>
  <tr>
    <td>Star</td>
    <td>A star is an astronomical object comprising a luminous spheroid of plasma held together by its gravity.</td>
  </tr>
  <tr>
    <td>Quasar</td>
    <td>A quasar (also known as a quasi-stellar object, abbreviated QSO) is an extremely luminous active galactic nucleus (AGN), powered by a supermassive black hole, with mass ranging from millions to tens of billions of solar masses, surrounded by a gaseous accretion disc.The term quasar originated as a contraction of "quasi-stellar [star-like] radio source"—because quasars were first identified during the 1950s as sources of radio-wave emission of unknown physical origin—and when identified in photographic images at visible wavelengths, they resembled faint, star-like points of light.</td>
  </tr>
  <tr>
    <td>Galaxy</td>
    <td>A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas, dust, and dark matter.</td>
  </tr>
</table>

<h2>References:</h2>

<ol>
  <li>"star." Oxford Dictionary of English 2e, Oxford University Press, 2003. </li>
  <li>"Galaxy" (İngilizce). Encyclopædia Britannica.</li>
  <li>Hupp, E. (21 Ağustos 2006). "NASA Finds Direct Proof of Dark Matter"</li>
  <li>Wu, Xue-Bing; Wang, Feige; Fan, Xiaohui; Yi, Weimin; Zuo, Wenwen; Bian, Fuyan; Jiang, Linhua; McGreer, Ian D.; Wang, Ran; Yang, Jinyi; Yang, Qian (Şubat 2015). "An ultraluminous quasar with a twelve-billion-solar-mass black hole at redshift 6.30". Nature (İngilizce). 518 (7540): 512-515. doi:10.1038/nature14241. ISSN 1476-4687</li>
  <li>Frank, Juhan; King, Andrew; Raine, Derek J. (1 Ocak 2002). Accretion Power in Astrophysics: Third Edition</li>
</ol>

## Content

<p>The data consists of 100,000 observations of space taken by the SDSS (Sloan Digital Sky Survey). Every observation is described by 17 feature columns and 1 class column which identifies it to be either a star, galaxy or quasar.</p>

<table>
  <tr>
    <th><b><em><strong>Feature</strong></em></b></th>
    <th><b><em><strong>Description</strong></em></b></th>
  </tr>
  <tr>
    <td>obj_ID</td>
    <td>Object Identifier, the unique value that identifies the object in the image catalog used by the CAS</td>
  </tr>
  <tr>
    <td>alpha</td>
    <td>Right Ascension angle (at J2000 epoch)</td>
  </tr>
  <tr>
    <td>delta</td>
    <td>Declination angle (at J2000 epoch)</td>
  </tr>
  <tr>
    <td>u</td>
    <td>Ultraviolet filter in the photometric system</td>
  </tr>
  <tr>
    <td>g</td>
    <td>Green filter in the photometric system</td>
  </tr>
  <tr>
    <td>r</td>
    <td>Red filter in the photometric system</td>
  </tr>
  <tr>
    <td>i</td>
    <td>Near Infrared filter in the photometric system</td>
  </tr>
  <tr>
    <td>z</td>
    <td>Infrared filter in the photometric system</td>
  </tr>
  <tr>
    <td>run_ID</td>
    <td>Run Number used to identify the specific scan</td>
  </tr>
  <tr>
    <td>rerun_ID</td>
    <td>Rerun Number to specify how the image was processed</td>
  </tr>
  <tr>
    <td>cam_col</td>
    <td>Camera column to identify the scanline within the run</td>
  </tr>
  <tr>
    <td>field_ID</td>
    <td>Field number to identify each field</td>
  </tr>
  <tr>
    <td>spec_obj_ID</td>
    <td>Unique ID used for optical spectroscopic objects (this means that 2 different observations with the same spec_obj_ID must share the output class)</td>
  </tr>
  <tr>
    <td>class</td>
    <td>Object class (galaxy, star or quasar object)</td>
  </tr>
  <tr>
    <td>redshift</td>
    <td>Redshift value based on the increase in wavelength</td>
  </tr>
  <tr>
    <td>plate</td>
    <td>Plate ID, identifies each plate in SDSS</td>
  </tr>
  <tr>
    <td>MJD</td>
    <td>Modified Julian Date, used to indicate when a given piece of SDSS data was taken</td>
  </tr>
  <tr>
    <td>fiber_ID</td>
    <td>Fiber ID that identifies the fiber that pointed the light at the focal plane in each observation</td>
  </tr>
</table>

## Acknowledgements

<p>The data released by the SDSS is under public domain. Its taken from the current data release RD17.</p>

    More information about the license: http://www.sdss.org/science/image-gallery/

<p>SDSS Publications:</p>

    Abdurro’uf et al., The Seventeenth data release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 DATA (Abdurro’uf et al. submitted to ApJS) [arXiv:2112.02026]


