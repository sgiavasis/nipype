"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class DWIUnbiasedNonLocalMeansFilterInputSpec(CommandLineInputSpec):
    rs = InputMultiPath(traits.Int, desc="The algorithm search for similar voxels in a neighborhood of this size (larger sizes than the default one are extremely slow).", sep=",", argstr="--rs %s")
    rc = InputMultiPath(traits.Int, desc="Similarity between blocks is measured using windows of this size.", sep=",", argstr="--rc %s")
    hp = traits.Float(desc="This parameter is related to noise; the larger the parameter, the more agressive the filtering. Should be near 1, and only values between 0.8 and 1.2 are allowed", argstr="--hp %f")
    ng = traits.Int(desc="The number of the closest gradients that are used to jointly filter a given gradient direction (a maximum of 5 is allowed).", argstr="--ng %d")
    re = InputMultiPath(traits.Int, desc="A neighborhood of this size is used to compute the statistics for noise estimation.", sep=",", argstr="--re %s")
    outputVolume = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Output DWI volume.", argstr="%s")


class DWIUnbiasedNonLocalMeansFilterOutputSpec(TraitedSpec):
    outputVolume = File(position=-1, desc="Output DWI volume.", exists=True)


class DWIUnbiasedNonLocalMeansFilter(SEMLikeCommandLine):
    """title: DWI Unbiased Non Local Means Filter

category: Legacy.Diffusion.Denoising

description: This module reduces noise (or unwanted detail) on a set of diffusion weighted images. For this, it filters the images using a Unbiased Non Local Means for Rician noise algorithm. It exploits not only the spatial redundancy, but the redundancy in similar gradient directions as well; it takes into account the N closest gradient directions to the direction being processed (a maximum of 5 gradient directions is allowed to keep a reasonable computational load, since we do not use neither similarity maps nor block-wise implementation).
The noise parameter is automatically estimated in the same way as in the jointLMMSE module.
A complete description of the algorithm may be found in:
Antonio Tristan-Vega and Santiago Aja-Fernandez, DWI filtering using joint information for DTI and HARDI, Medical Image Analysis, Volume 14, Issue 2, Pages 205-218. 2010.
Please, note that the execution of this filter is extremely slow, son only very conservative parameters (block size and search size as small as possible) should be used. Even so, its execution may take several hours. The advantage of this filter over joint LMMSE is its better preservation of edges and fine structures.

version: 0.0.1.$Revision: 1 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/UnbiasedNonLocalMeansFilterForDWI

contributor: Antonio Tristan Vega (UVa), Santiago Aja Fernandez (UVa)

acknowledgements: Partially founded by grant number TEC2007-67073/TCM from the Comision Interministerial de Ciencia y Tecnologia (Spain).

"""

    input_spec = DWIUnbiasedNonLocalMeansFilterInputSpec
    output_spec = DWIUnbiasedNonLocalMeansFilterOutputSpec
    _cmd = "/home/raid3/gorgolewski/software/slicer/Slicer --launch DWIUnbiasedNonLocalMeansFilter "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
